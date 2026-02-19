"use client";

import { useState, useEffect, useContext } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "../contexts/AuthContext";
import { ThemeContext } from "../ThemeContext";
import {
  Plus,
  Database,
  Trash2,
  CheckCircle,
  Info,
  Eye,
  EyeOff,
} from "lucide-react";
import Navbar from "../components/Navbar";
import api from "../../lib/api";

export default function ConnectionsPage() {
  const { user } = useAuth();
  const router = useRouter();
  const { isDark } = useContext(ThemeContext);
  const [connections, setConnections] = useState([]);
  const [showModal, setShowModal] = useState(false);
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState({
    provider: "postgres",
    user: "",
    password: "",
    host: "",
    db_name: "",
    port: 5432,
  });
  const [testResult, setTestResult] = useState(null);
  const [selectedSchemas, setSelectedSchemas] = useState([]);
  const [tablesViews, setTablesViews] = useState([]);
  const [selectedTables, setSelectedTables] = useState([]);
  const [selectedClient, setSelectedClient] = useState(null);
  const [clients, setClients] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [showInfoModal, setShowInfoModal] = useState(false);
  const [selectedDatabase, setSelectedDatabase] = useState(null);
  const [dbDescription, setDbDescription] = useState("");
  const [tableDescriptions, setTableDescriptions] = useState({});
  const [showPassword, setShowPassword] = useState(false);

  const canManageDB =
    user?.role === "internal_superuser" || user?.role === "client";
  const isSuperuser = user?.role === "internal_superuser";

  useEffect(() => {
    fetchConnections();
    if (isSuperuser) {
      fetchClients();
    }
  }, [isSuperuser]);

  const fetchConnections = async () => {
    try {
      const res = await api.get("/databases");
      setConnections(res.data);
    } catch (err) {
      console.error("Failed to fetch connections:", err);
    }
  };

  const fetchClients = async () => {
    try {
      const res = await api.get("/clients");
      setClients(res.data);
    } catch (err) {
      console.error("Failed to fetch clients:", err);
    }
  };

  const handleConnect = async (conn) => {
    try {
      await api.post("/database/connect", { database_id: conn.id });
      router.push("/dashboard");
    } catch (err) {
      console.error("Failed to connect:", err);
      alert("Failed to connect to database: " + (err.response?.data?.detail || err.message));
    }
  };

  const handleTestConnection = async () => {
    setLoading(true);
    setError("");
    try {
      const res = await api.post("/databases/test-connection", formData);
      setTestResult(res.data);
      setStep(2);
    } catch (err) {
      setError(err.response?.data?.detail || "Connection failed");
      setTestResult(null);
    } finally {
      setLoading(false);
    }
  };

  const handleSchemaSelection = async () => {
    if (selectedSchemas.length === 0) {
      setError("Please select at least one schema");
      return;
    }
    setLoading(true);
    setError("");
    try {
      const res = await api.post("/databases/get-tables-views", {
        ...formData,
        schemas: selectedSchemas
      });
      setTablesViews(res.data.tables_views);
      setStep(3);
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to fetch tables");
    } finally {
      setLoading(false);
    }
  };

  const handleSchemaToggle = (schema) => {
    setSelectedSchemas((prev) =>
      prev.includes(schema) ? prev.filter((s) => s !== schema) : [...prev, schema]
    );
  };

  const handleTableToggle = (fullName) => {
    setSelectedTables((prev) =>
      prev.includes(fullName) ? prev.filter((t) => t !== fullName) : [...prev, fullName]
    );
  };

  const handleSelectAllSchemas = (checked) => {
    setSelectedSchemas(checked ? testResult.schemas : []);
  };

  const handleSelectAll = (checked) => {
    setSelectedTables(checked ? tablesViews.map(tv => tv.full_name) : []);
  };

  const handleSaveDatabase = async () => {
    setLoading(true);
    setError("");
    try {
      const schemaRes = await api.post("/databases/generate-schema", {
        ...formData,
        selected_tables: selectedTables
      });
      
      const tableDescObj = {};
      tablesViews.forEach(tv => {
        if (selectedTables.includes(tv.full_name)) {
          tableDescObj[tv.full_name] = {
            description: tableDescriptions[tv.full_name] || "",
            type: tv.type,
            schema: tv.schema
          };
        }
      });
      
      const payload = {
        ...formData,
        selected_tables: selectedTables,
        description: tableDescObj,
        schema: schemaRes.data.schema,
        ...(isSuperuser && { client_id: selectedClient }),
      };
      await api.post("/databases", payload);
      await fetchConnections();
      resetForm();
      setShowModal(false);
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to save database");
    } finally {
      setLoading(false);
    }
  };

  const resetForm = () => {
    setFormData({
      provider: "postgres",
      user: "",
      password: "",
      host: "",
      db_name: "",
      port: 5432,
      title: "",
    });
    setTestResult(null);
    setSelectedSchemas([]);
    setTablesViews([]);
    setSelectedTables([]);
    setSelectedClient(null);
    setStep(1);
    setError("");
    setShowPassword(false);
  };

  const handleDelete = async (id) => {
    if (!confirm("Delete this connection?")) return;
    try {
      await api.delete(`/databases/${id}`);
      await fetchConnections();
    } catch (err) {
      const errorMsg = err.response?.data?.detail || "Failed to delete connection";
      alert(errorMsg);
      console.error("Failed to delete:", err);
    }
  };

  const handleOpenInfo = async (conn) => {
    setSelectedDatabase(conn);
    setDbDescription(conn.db_description || "");
    
    // Extract descriptions from the stored format
    const extractedDescriptions = {};
    if (conn.description) {
      Object.keys(conn.description).forEach(tableName => {
        if (typeof conn.description[tableName] === 'object' && conn.description[tableName].description !== undefined) {
          extractedDescriptions[tableName] = conn.description[tableName].description;
        } else {
          extractedDescriptions[tableName] = conn.description[tableName] || "";
        }
      });
    }
    
    setTableDescriptions(extractedDescriptions);
    setShowInfoModal(true);
  };

  const handleRemoveTable = (tableToRemove) => {
    const updatedDescriptions = { ...tableDescriptions };
    delete updatedDescriptions[tableToRemove];
    setTableDescriptions(updatedDescriptions);
    
    const updatedTables = selectedDatabase.selected_tables.filter(table => table !== tableToRemove);
    setSelectedDatabase({
      ...selectedDatabase,
      selected_tables: updatedTables
    });
  };

  const handleSaveInfo = async () => {
    setLoading(true);
    setError("");
    try {
      // Reconstruct the description object with the proper format
      const updatedDescriptions = {};
      Object.keys(tableDescriptions).forEach(tableName => {
        const existingData = selectedDatabase.description?.[tableName] || {};
        updatedDescriptions[tableName] = {
          description: tableDescriptions[tableName] || "",
          type: existingData.type || "table",
          schema: existingData.schema || tableName.split('.')[0]
        };
      });
      
      await api.put(`/databases/${selectedDatabase.id}`, {
        db_description: dbDescription,
        description: updatedDescriptions,
        selected_tables: selectedDatabase.selected_tables,
      });
      await fetchConnections();
      setShowInfoModal(false);
    } catch (err) {
      setError(err.response?.data?.detail || "Failed to update");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div
      className={`flex h-screen flex-col ${
        isDark ? "bg-gray-950" : "bg-gray-50"
      }`}
    >
      <Navbar />

      <div className="flex-1 overflow-auto p-6">
        <div className="mx-auto max-w-6xl">
          <div className="mb-6 flex items-center justify-between">
            <h1
              className={`text-2xl font-bold ${
                isDark ? "text-white" : "text-gray-900"
              }`}
            >
              Database Connections
            </h1>
            {canManageDB && (
              <button
                onClick={() => setShowModal(true)}
                className="flex items-center gap-2 rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
              >
                <Plus size={18} />
                Add Connection
              </button>
            )}
          </div>

          {connections.length === 0 ? (
            <div
              className={`flex h-96 items-center justify-center rounded-lg border ${
                isDark
                  ? "border-gray-800 bg-gray-900"
                  : "border-gray-200 bg-white"
              }`}
            >
              <div className="text-center">
                <Database className="mx-auto mb-4 text-gray-400" size={64} />
                <h3
                  className={`text-lg font-semibold mb-2 ${
                    isDark ? "text-white" : "text-gray-900"
                  }`}
                >
                  No Database Connections
                </h3>
                <p
                  className={`mb-4 ${
                    isDark ? "text-gray-400" : "text-gray-600"
                  }`}
                >
                  You haven't added any database connections yet.
                </p>
                {canManageDB && (
                  <button
                    onClick={() => setShowModal(true)}
                    className="flex items-center gap-2 mx-auto rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
                  >
                    <Plus size={18} />
                    Add Your First Database
                  </button>
                )}
              </div>
            </div>
          ) : (
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
              {connections.map((conn) => (
                <div
                  key={conn.id}
                  onClick={() => handleConnect(conn)}
                  className={`rounded-lg border p-4 cursor-pointer transition-colors ${
                    isDark
                      ? "border-gray-800 bg-gray-900 hover:bg-gray-800"
                      : "border-gray-200 bg-white hover:bg-gray-50"
                  }`}
                >
                  <div className="flex items-start justify-between">
                    <div className="flex items-center gap-3">
                      <Database className="text-blue-600" size={24} />
                      <div>
                        <h3
                          className={`font-semibold ${
                            isDark ? "text-white" : "text-gray-900"
                          }`}
                        >
                          {conn.title || conn.db_name}
                        </h3>
                        <p
                          className={`text-sm ${
                            isDark ? "text-gray-400" : "text-gray-600"
                          }`}
                        >
                          {conn.provider} • {conn.host}:{conn.port}
                        </p>
                      </div>
                    </div>
                    <div className="flex gap-2">
                      <button
                        onClick={(e) => {
                          e.stopPropagation();
                          handleOpenInfo(conn);
                        }}
                        className={`hover:text-blue-600 ${
                          isDark ? "text-gray-400" : "text-gray-600"
                        }`}
                        title="View/Edit Info"
                      >
                        <Info size={18} />
                      </button>
                      {canManageDB && (
                        <button
                          onClick={(e) => {
                            e.stopPropagation();
                            handleDelete(conn.id);
                          }}
                          className={`hover:text-red-600 ${
                            isDark ? "text-gray-400" : "text-gray-600"
                          }`}
                          title="Delete"
                        >
                          <Trash2 size={18} />
                        </button>
                      )}
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {showModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4 overflow-auto">
          <div
            className={`w-full max-h-[90vh] overflow-y-scroll max-w-2xl rounded-lg p-6 my-8 ${
              isDark ? "bg-gray-900" : "bg-white"
            }`}
          >
            <h2
              className={`mb-4 text-xl font-bold ${
                isDark ? "text-white" : "text-gray-900"
              }`}
            >
              {step === 1
                ? "Test Connection"
                : step === 2
                ? "Select Schemas"
                : step === 3
                ? "Select Tables & Views"
                : "Add Descriptions"}
            </h2>

            {step === 1 && (
              <div className="space-y-4">
                <div>
                  <label
                    className={`block text-sm font-medium ${
                      isDark ? "text-gray-300" : "text-gray-700"
                    }`}
                  >
                    Title
                  </label>
                  <input
                    type="text"
                    value={formData.title || ""}
                    onChange={(e) =>
                      setFormData({ ...formData, title: e.target.value })
                    }
                    placeholder="Connection title (optional)"
                    className={`mt-1 w-full rounded-lg border px-3 py-2 ${
                      isDark
                        ? "border-gray-600 bg-gray-800 text-white"
                        : "border-gray-300"
                    }`}
                  />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label
                      className={`block text-sm font-medium ${
                        isDark ? "text-gray-300" : "text-gray-700"
                      }`}
                    >
                      Provider
                    </label>
                    <select
                      value={formData.provider}
                      onChange={(e) =>
                        setFormData({ ...formData, provider: e.target.value })
                      }
                      className={`mt-1 w-full rounded-lg border px-3 py-2 ${
                        isDark
                          ? "border-gray-600 bg-gray-800 text-white"
                          : "border-gray-300"
                      }`}
                    >
                      <option value="postgres">PostgreSQL</option>
                      <option value="mysql">MySQL</option>
                      <option value="mssql">MSSQL</option>
                    </select>
                  </div>
                  <div>
                    <label
                      className={`block text-sm font-medium ${
                        isDark ? "text-gray-300" : "text-gray-700"
                      }`}
                    >
                      Database Name
                    </label>
                    <input
                      type="text"
                      value={formData.db_name}
                      onChange={(e) =>
                        setFormData({ ...formData, db_name: e.target.value })
                      }
                      className={`mt-1 w-full rounded-lg border px-3 py-2 ${
                        isDark
                          ? "border-gray-600 bg-gray-800 text-white"
                          : "border-gray-300"
                      }`}
                      required
                    />
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label
                      className={`block text-sm font-medium ${
                        isDark ? "text-gray-300" : "text-gray-700"
                      }`}
                    >
                      Host
                    </label>
                    <input
                      type="text"
                      value={formData.host}
                      onChange={(e) =>
                        setFormData({ ...formData, host: e.target.value })
                      }
                      className={`mt-1 w-full rounded-lg border px-3 py-2 ${
                        isDark
                          ? "border-gray-600 bg-gray-800 text-white"
                          : "border-gray-300"
                      }`}
                      required
                    />
                  </div>
                  <div>
                    <label
                      className={`block text-sm font-medium ${
                        isDark ? "text-gray-300" : "text-gray-700"
                      }`}
                    >
                      Port
                    </label>
                    <input
                      type="number"
                      value={formData.port}
                      onChange={(e) =>
                        setFormData({
                          ...formData,
                          port: parseInt(e.target.value),
                        })
                      }
                      className={`mt-1 w-full rounded-lg border px-3 py-2 ${
                        isDark
                          ? "border-gray-600 bg-gray-800 text-white"
                          : "border-gray-300"
                      }`}
                      required
                    />
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label
                      className={`block text-sm font-medium ${
                        isDark ? "text-gray-300" : "text-gray-700"
                      }`}
                    >
                      Username
                    </label>
                    <input
                      type="text"
                      value={formData.user}
                      onChange={(e) =>
                        setFormData({ ...formData, user: e.target.value })
                      }
                      className={`mt-1 w-full rounded-lg border px-3 py-2 ${
                        isDark
                          ? "border-gray-600 bg-gray-800 text-white"
                          : "border-gray-300"
                      }`}
                      required
                    />
                  </div>
                  <div>
                    <label
                      className={`block text-sm font-medium ${
                        isDark ? "text-gray-300" : "text-gray-700"
                      }`}
                    >
                      Password
                    </label>
                    <div className="relative">
                      <input
                        type={showPassword ? "text" : "password"}
                        value={formData.password}
                        onChange={(e) =>
                          setFormData({ ...formData, password: e.target.value })
                        }
                        className={`mt-1 w-full rounded-lg border px-3 py-2 pr-10 ${
                          isDark
                            ? "border-gray-600 bg-gray-800 text-white"
                            : "border-gray-300"
                        }`}
                        required
                      />
                      <button
                        type="button"
                        onClick={() => setShowPassword(!showPassword)}
                        className={`absolute right-3 top-1/2 -translate-y-1/2 mt-0.5 ${
                          isDark
                            ? "text-gray-400 hover:text-gray-300"
                            : "text-gray-500 hover:text-gray-700"
                        }`}
                      >
                        {showPassword ? (
                          <EyeOff size={18} />
                        ) : (
                          <Eye size={18} />
                        )}
                      </button>
                    </div>
                  </div>
                </div>
                {error && (
                  <div className="rounded-lg bg-red-50 p-3 text-sm text-red-800 dark:bg-red-900 dark:text-red-200">
                    {error}
                  </div>
                )}
                <div className="flex gap-2">
                  <button
                    onClick={handleTestConnection}
                    disabled={loading}
                    className="flex-1 rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 disabled:opacity-50"
                  >
                    {loading ? "Testing..." : "Test Connection"}
                  </button>
                  <button
                    onClick={() => {
                      setShowModal(false);
                      resetForm();
                    }}
                    className={`flex-1 rounded-lg border px-4 py-2 ${
                      isDark
                        ? "border-gray-600 hover:bg-gray-800 text-white"
                        : "border-gray-300 hover:bg-gray-50"
                    }`}
                  >
                    Cancel
                  </button>
                </div>
              </div>
            )}

            {step === 2 && testResult && (
              <div className="space-y-4">
                <div className="flex items-center gap-2 rounded-lg bg-green-50 p-3 text-green-800 dark:bg-green-900 dark:text-green-200">
                  <CheckCircle size={18} />
                  <span>{testResult.message}</span>
                </div>
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <label
                      className={`block text-sm font-medium ${
                        isDark ? "text-gray-300" : "text-gray-700"
                      }`}
                    >
                      Select Schemas ({selectedSchemas.length}/
                      {testResult.schemas.length})
                    </label>
                    <label className="flex items-center gap-2 cursor-pointer">
                      <input
                        type="checkbox"
                        checked={
                          selectedSchemas.length === testResult.schemas.length
                        }
                        onChange={(e) => handleSelectAllSchemas(e.target.checked)}
                        className="rounded"
                      />
                      <span
                        className={`text-sm ${
                          isDark ? "text-gray-300" : "text-gray-700"
                        }`}
                      >
                        Select All
                      </span>
                    </label>
                  </div>
                  <div
                    className={`max-h-96 overflow-auto rounded-lg border p-3 space-y-2 ${
                      isDark ? "border-gray-600 bg-gray-800" : "border-gray-300"
                    }`}
                  >
                    {testResult.schemas.map((schema) => (
                      <label
                        key={schema}
                        className={`flex items-center gap-2 cursor-pointer p-2 rounded ${
                          isDark ? "hover:bg-gray-700" : "hover:bg-gray-100"
                        }`}
                      >
                        <input
                          type="checkbox"
                          checked={selectedSchemas.includes(schema)}
                          onChange={() => handleSchemaToggle(schema)}
                          className="rounded"
                        />
                        <span
                          className={isDark ? "text-white" : "text-gray-900"}
                        >
                          {schema}
                        </span>
                      </label>
                    ))}
                  </div>
                </div>
                <div className="flex gap-2">
                  <button
                    onClick={handleSchemaSelection}
                    disabled={selectedSchemas.length === 0 || loading}
                    className="flex-1 rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 disabled:opacity-50"
                  >
                    {loading ? "Loading..." : "Next"}
                  </button>
                  <button
                    onClick={() => setStep(1)}
                    className={`flex-1 rounded-lg border px-4 py-2 ${
                      isDark
                        ? "border-gray-600 hover:bg-gray-800 text-white"
                        : "border-gray-300 hover:bg-gray-50"
                    }`}
                  >
                    Back
                  </button>
                </div>
              </div>
            )}

            {step === 3 && tablesViews.length > 0 && (
              <div className="space-y-4">
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <label
                      className={`block text-sm font-medium ${
                        isDark ? "text-gray-300" : "text-gray-700"
                      }`}
                    >
                      Select Tables & Views ({selectedTables.length}/
                      {tablesViews.length})
                    </label>
                    <label className="flex items-center gap-2 cursor-pointer">
                      <input
                        type="checkbox"
                        checked={
                          selectedTables.length === tablesViews.length
                        }
                        onChange={(e) => handleSelectAll(e.target.checked)}
                        className="rounded"
                      />
                      <span
                        className={`text-sm ${
                          isDark ? "text-gray-300" : "text-gray-700"
                        }`}
                      >
                        Select All
                      </span>
                    </label>
                  </div>
                  <div
                    className={`max-h-96 overflow-auto rounded-lg border p-3 space-y-2 ${
                      isDark ? "border-gray-600 bg-gray-800" : "border-gray-300"
                    }`}
                  >
                    {tablesViews.map((tv) => (
                      <label
                        key={tv.full_name}
                        className={`flex items-center gap-2 cursor-pointer p-2 rounded ${
                          isDark ? "hover:bg-gray-700" : "hover:bg-gray-100"
                        }`}
                      >
                        <input
                          type="checkbox"
                          checked={selectedTables.includes(tv.full_name)}
                          onChange={() => handleTableToggle(tv.full_name)}
                          className="rounded"
                        />
                        <span
                          className={isDark ? "text-white" : "text-gray-900"}
                        >
                          {tv.full_name}
                        </span>
                        <span
                          className={`ml-auto text-xs px-2 py-1 rounded ${
                            tv.type === "view"
                              ? isDark
                                ? "bg-purple-900 text-purple-200"
                                : "bg-purple-100 text-purple-800"
                              : isDark
                              ? "bg-blue-900 text-blue-200"
                              : "bg-blue-100 text-blue-800"
                          }`}
                        >
                          {tv.type}
                        </span>
                      </label>
                    ))}
                  </div>
                </div>
                <div className="flex gap-2">
                  <button
                    onClick={() => setStep(4)}
                    disabled={selectedTables.length === 0}
                    className="flex-1 rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 disabled:opacity-50"
                  >
                    Next
                  </button>
                  <button
                    onClick={() => setStep(2)}
                    className={`flex-1 rounded-lg border px-4 py-2 ${
                      isDark
                        ? "border-gray-600 hover:bg-gray-800 text-white"
                        : "border-gray-300 hover:bg-gray-50"
                    }`}
                  >
                    Back
                  </button>
                </div>
              </div>
            )}

            {step === 4 && (
              <div className="space-y-4">
                <div>
                  <label
                    className={`block text-sm font-medium mb-2 ${
                      isDark ? "text-gray-300" : "text-gray-700"
                    }`}
                  >
                    Database Description
                  </label>
                  <textarea
                    value={dbDescription}
                    onChange={(e) => setDbDescription(e.target.value)}
                    placeholder="Add overall database description..."
                    rows={3}
                    className={`w-full rounded-lg border px-3 py-2 resize-none ${
                      isDark
                        ? "border-gray-600 bg-gray-800 text-white placeholder-gray-500"
                        : "border-gray-300 placeholder-gray-400"
                    }`}
                  />
                </div>
                <div>
                  <label
                    className={`block text-sm font-medium mb-3 ${
                      isDark ? "text-gray-300" : "text-gray-700"
                    }`}
                  >
                    Table/View Descriptions ({selectedTables.length})
                  </label>
                  <div className="max-h-96 overflow-auto space-y-3">
                    {selectedTables.map((fullName) => {
                      const tv = tablesViews.find(t => t.full_name === fullName);
                      return (
                        <div
                          key={fullName}
                          className={`rounded-lg border p-3 ${
                            isDark
                              ? "border-gray-600 bg-gray-800"
                              : "border-gray-200 bg-gray-50"
                          }`}
                        >
                          <div className="flex items-center gap-2 mb-2">
                            <label
                              className={`text-sm font-semibold ${
                                isDark ? "text-blue-400" : "text-blue-600"
                              }`}
                            >
                              {fullName}
                            </label>
                            <span
                              className={`text-xs px-2 py-0.5 rounded ${
                                tv?.type === "view"
                                  ? isDark
                                    ? "bg-purple-900 text-purple-200"
                                    : "bg-purple-100 text-purple-800"
                                  : isDark
                                  ? "bg-blue-900 text-blue-200"
                                  : "bg-blue-100 text-blue-800"
                              }`}
                            >
                              {tv?.type || "table"}
                            </span>
                          </div>
                          <textarea
                            placeholder="Describe this table/view..."
                            value={tableDescriptions[fullName] || ""}
                            onChange={(e) =>
                              setTableDescriptions({
                                ...tableDescriptions,
                                [fullName]: e.target.value,
                              })
                            }
                            rows={2}
                            className={`w-full rounded border px-3 py-2 text-sm resize-none ${
                              isDark
                                ? "border-gray-600 bg-gray-700 text-white placeholder-gray-500"
                                : "border-gray-300 placeholder-gray-400"
                            }`}
                          />
                        </div>
                      );
                    })}
                  </div>
                </div>
                {isSuperuser && (
                  <div>
                    <label
                      className={`block text-sm font-medium mb-2 ${
                        isDark ? "text-gray-300" : "text-gray-700"
                      }`}
                    >
                      Select Client *
                    </label>
                    <select
                      value={selectedClient || ""}
                      onChange={(e) =>
                        setSelectedClient(parseInt(e.target.value))
                      }
                      className={`w-full rounded-lg border px-3 py-2 ${
                        isDark
                          ? "border-gray-600 bg-gray-800 text-white"
                          : "border-gray-300"
                      }`}
                      required
                    >
                      <option value="">Choose a client</option>
                      {clients.map((client) => (
                        <option key={client.id} value={client.id}>
                          {client.client_name}
                        </option>
                      ))}
                    </select>
                  </div>
                )}
                {error && (
                  <div className="rounded-lg bg-red-50 p-3 text-sm text-red-800 dark:bg-red-900 dark:text-red-200">
                    {error}
                  </div>
                )}
                <div className="flex gap-2">
                  <button
                    onClick={handleSaveDatabase}
                    disabled={loading || (isSuperuser && !selectedClient)}
                    className="flex-1 rounded-lg bg-green-600 px-4 py-2 text-white hover:bg-green-700 disabled:opacity-50"
                  >
                    {loading ? "Saving..." : "Save Database"}
                  </button>
                  <button
                    onClick={() => setStep(3)}
                    className={`flex-1 rounded-lg border px-4 py-2 ${
                      isDark
                        ? "border-gray-600 hover:bg-gray-800 text-white"
                        : "border-gray-300 hover:bg-gray-50"
                    }`}
                  >
                    Back
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {showInfoModal && selectedDatabase && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4 overflow-hidden">
          <div
            className={`w-full max-w-4xl h-[90vh] flex flex-col rounded-lg ${
              isDark ? "bg-gray-900" : "bg-white"
            }`}
          >
            <div
              className={`p-6 border-b ${
                isDark ? "border-gray-700" : "border-gray-200"
              }`}
            >
              <h2
                className={`text-xl font-bold ${
                  isDark ? "text-white" : "text-gray-900"
                }`}
              >
                Database Information - {selectedDatabase.db_name}
              </h2>
            </div>

            <div className="flex-1 overflow-y-auto p-6 space-y-6" onScroll={(e) => e.stopPropagation()}>
              <div>
                <label
                  className={`block text-sm font-medium mb-2 ${
                    isDark ? "text-gray-300" : "text-gray-700"
                  }`}
                >
                  Database Description
                </label>
                <textarea
                  value={dbDescription}
                  onChange={(e) => setDbDescription(e.target.value)}
                  placeholder="Add a comprehensive description for this database..."
                  rows={4}
                  className={`w-full rounded-lg border px-3 py-2 resize-none ${
                    isDark
                      ? "border-gray-600 bg-gray-800 text-white placeholder-gray-500"
                      : "border-gray-300 placeholder-gray-400"
                  }`}
                />
              </div>

              {selectedDatabase.selected_tables &&
                selectedDatabase.selected_tables.length > 0 && (
                  <div>
                    <label
                      className={`block text-sm font-medium mb-3 ${
                        isDark ? "text-gray-300" : "text-gray-700"
                      }`}
                    >
                      Table Descriptions (
                      {selectedDatabase.selected_tables.length} tables)
                    </label>
                    <div className="space-y-4">
                      {selectedDatabase.selected_tables.map((table) => (
                        <div
                          key={table}
                          className={`rounded-lg border p-4 ${
                            isDark
                              ? "border-gray-600 bg-gray-800"
                              : "border-gray-200 bg-gray-50"
                          }`}
                        >
                          <div className="flex items-center justify-between mb-2">
                            <label
                              className={`text-sm font-semibold ${
                                isDark ? "text-blue-400" : "text-blue-600"
                              }`}
                            >
                              {table}
                            </label>
                            <button
                              onClick={() => handleRemoveTable(table)}
                              className={`p-1 rounded hover:bg-red-100 ${
                                isDark ? "text-red-400 hover:bg-red-900/20" : "text-red-600"
                              }`}
                              title="Remove table"
                            >
                              <Trash2 size={16} />
                            </button>
                          </div>
                          <textarea
                            placeholder="Describe the purpose, structure, and key information about this table..."
                            value={tableDescriptions[table] || ""}
                            onChange={(e) =>
                              setTableDescriptions({
                                ...tableDescriptions,
                                [table]: e.target.value,
                              })
                            }
                            rows={3}
                            className={`w-full rounded border px-3 py-2 text-sm resize-none ${
                              isDark
                                ? "border-gray-600 bg-gray-700 text-white placeholder-gray-500"
                                : "border-gray-300 placeholder-gray-400"
                            }`}
                          />
                        </div>
                      ))}
                    </div>
                  </div>
                )}
            </div>

            <div
              className={`p-6 border-t ${
                isDark ? "border-gray-700" : "border-gray-200"
              }`}
            >
              {error && (
                <div className="rounded-lg bg-red-50 p-3 text-sm text-red-800 dark:bg-red-900 dark:text-red-200 mb-4">
                  {error}
                </div>
              )}
              <div className="flex gap-3">
                <button
                  onClick={handleSaveInfo}
                  disabled={loading}
                  className="flex-1 rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 disabled:opacity-50 font-medium"
                >
                  {loading ? "Saving..." : "Save Changes"}
                </button>
                <button
                  onClick={() => setShowInfoModal(false)}
                  className={`flex-1 rounded-lg border px-4 py-2 font-medium ${
                    isDark
                      ? "border-gray-600 hover:bg-gray-800 text-white"
                      : "border-gray-300 hover:bg-gray-50 text-gray-900"
                  }`}
                >
                  Cancel
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
