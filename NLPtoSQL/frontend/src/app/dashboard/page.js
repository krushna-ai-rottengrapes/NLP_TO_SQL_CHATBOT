"use client";

import { useState, useEffect, useContext } from "react";
import { useAuth } from "../contexts/AuthContext";
import { ThemeContext } from "../ThemeContext";
import { useRouter } from "next/navigation";
import { Plus, Eye, LayoutDashboard, Database, Trash2 } from "lucide-react";
import Navbar from "../components/Navbar";
import api from "../../lib/api";

export default function DashboardPage() {
  const { user, isOwner, loading } = useAuth();
  // console.log("User:", user);
  const { isDark } = useContext(ThemeContext);
  const router = useRouter();
  const [dashboards, setDashboards] = useState([]);
  const [databases, setDatabases] = useState([]);
  const [showDbModal, setShowDbModal] = useState(false);
  const [selectedDb, setSelectedDb] = useState(null);
  const [connecting, setConnecting] = useState(null);
  const [deleting, setDeleting] = useState(null);

  useEffect(() => {
    if (!loading) {
      fetchDashboards();
      fetchDatabases();
    }
  }, [loading]);

  if (loading) {
    return null;
  }

  const fetchDashboards = async () => {
    try {
      const res = await api.get("/dashboards");
      setDashboards(res.data);
    } catch (err) {
      console.error("Failed to fetch dashboards:", err);
    }
  };

  const fetchDatabases = async () => {
    try {
      const res = await api.get("/databases");
      setDatabases(res.data);
    } catch (err) {
      console.error("Failed to fetch databases:", err);
    }
  };

  const handleCreateNew = () => {
    if (databases.length === 0) {
      alert("Please add a database connection first");
      router.push("/connections");
      return;
    }
    setShowDbModal(true);
  };

  const handleSelectDatabase = async () => {
    if (!selectedDb) return;
    await handleConnectDatabase(selectedDb);
  };

  const handleConnectDatabase = async (dbId) => {
    setConnecting(dbId);
    try {
      await api.post("/database/connect", { database_id: dbId });
      setShowDbModal(false);
      setSelectedDb(null);
      router.push(`/studio?db_id=${dbId}`);
    } catch (err) {
      alert(err.response?.data?.detail || "Failed to connect to database");
    } finally {
      setConnecting(null);
    }
  };

  const handleView = async (dashboard) => {
    if (dashboard.db_id) {
      setConnecting(dashboard.db_id);
      try {
        await api.post("/database/connect", { database_id: dashboard.db_id });
        router.push(
          `/studio?dashboard_id=${dashboard.id}&db_id=${dashboard.db_id}`
        );
      } catch (err) {
        alert(err.response?.data?.detail || "Failed to connect to database");
      } finally {
        setConnecting(null);
      }
    } else {
      router.push(`/studio?dashboard_id=${dashboard.id}`);
    }
  };

  const handleDelete = async (dashboardId) => {
    if (!confirm("Are you sure you want to delete this dashboard?")) return;

    setDeleting(dashboardId);
    try {
      await api.delete(`/dashboards/${dashboardId}`);
      setDashboards(dashboards.filter((d) => d.id !== dashboardId));
    } catch (err) {
      alert(err.response?.data?.detail || "Failed to delete dashboard");
    } finally {
      setDeleting(null);
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
              Dashboards
            </h1>
            {isOwner() && (
              <button
                onClick={handleCreateNew}
                className="flex items-center gap-2 rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
              >
                <Plus size={18} />
                Create New
              </button>
            )}
          </div>

          {dashboards.length === 0 ? (
            <div
              className={`flex h-64 items-center justify-center rounded-lg border ${
                isDark
                  ? "border-gray-800 bg-gray-900"
                  : "border-gray-200 bg-white"
              }`}
            >
              <div className="text-center">
                <LayoutDashboard
                  className="mx-auto mb-4 text-gray-400"
                  size={48}
                />
                <p className={`${isDark ? "text-gray-400" : "text-gray-600"}`}>
                  No dashboards yet. {isOwner() && "Create your first one!"}
                </p>
              </div>
            </div>
          ) : (
            <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
              {dashboards.map((dashboard) => (
                <div
                  key={dashboard.id}
                  className={`rounded-lg border p-6 hover:shadow-lg ${
                    isDark
                      ? "border-gray-800 bg-gray-900"
                      : "border-gray-200 bg-white"
                  }`}
                >
                  <div className="mb-4 flex items-start justify-between">
                    <div>
                      <h3
                        className={`font-semibold ${
                          isDark ? "text-white" : "text-gray-900"
                        }`}
                      >
                        {dashboard.title || "Untitled Dashboard"}
                      </h3>
                      <p
                        className={`mt-1 text-sm ${
                          isDark ? "text-gray-400" : "text-gray-600"
                        }`}
                      >
                        Created{" "}
                        {new Date(dashboard?.created_at).toLocaleDateString()}
                      </p>
                    </div>
                    <LayoutDashboard className="text-blue-600" size={24} />
                  </div>

                  <div className="flex gap-2">
                    <button
                      onClick={() => handleView(dashboard)}
                      disabled={connecting === dashboard.db_id}
                      className={`flex flex-1 items-center justify-center gap-2 rounded-lg border px-4 py-2 text-sm disabled:opacity-50 ${
                        isDark
                          ? "border-gray-600 hover:bg-gray-800 text-white"
                          : "border-gray-300 hover:bg-gray-50 text-gray-900"
                      }`}
                    >
                      <Eye size={16} />
                      {connecting === dashboard.db_id
                        ? "Connecting..."
                        : "View"}
                    </button>
                    {isOwner() && (
                      <button
                        onClick={() => handleDelete(dashboard.id)}
                        disabled={deleting === dashboard.id}
                        className={`rounded-lg border px-3 py-2 text-sm disabled:opacity-50 ${
                          isDark
                            ? "border-red-600 text-red-500 hover:bg-red-900/20"
                            : "border-red-300 text-red-600 hover:bg-red-50"
                        }`}
                      >
                        <Trash2 size={16} />
                      </button>
                    )}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>

      {showDbModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4 ">
          <div
            className={`w-full max-w-md rounded-lg p-6 h-[90vh] overflow-y-scroll ${
              isDark ? "bg-gray-900" : "bg-white"
            }`}
          >
            <h2
              className={`mb-4 text-xl font-bold ${
                isDark ? "text-white" : "text-gray-900"
              }`}
            >
              Select Database
            </h2>

            <div className="space-y-4 mb-6">
              <div className="space-y-3">
                {databases.map((db) => (
                  <label
                    key={db.id}
                    className={`flex items-center gap-3 p-3 rounded-lg border cursor-pointer transition-colors ${
                      selectedDb === db.id
                        ? isDark
                          ? "border-blue-500 bg-blue-900/20"
                          : "border-blue-500 bg-blue-50"
                        : isDark
                        ? "border-gray-600 hover:bg-gray-800"
                        : "border-gray-300 hover:bg-gray-50"
                    }`}
                  >
                    <input
                      type="radio"
                      name="database"
                      value={db.id}
                      checked={selectedDb === db.id}
                      onChange={() => setSelectedDb(db.id)}
                      className="text-blue-600"
                    />
                    <Database className="text-blue-600" size={20} />
                    <div className="flex-1">
                      <div
                        className={`font-medium ${
                          isDark ? "text-white" : "text-gray-900"
                        }`}
                      >
                        {db?.title || db.db_name}
                      </div>
                      <div
                        className={`text-sm ${
                          isDark ? "text-gray-400" : "text-gray-600"
                        }`}
                      >
                        {db.provider} • {db.host}
                      </div>
                    </div>
                  </label>
                ))}
              </div>
            </div>

            <div className="flex gap-2">
              <button
                onClick={handleSelectDatabase}
                disabled={!selectedDb || connecting}
                className="flex-1 rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700 disabled:opacity-50 font-medium"
              >
                {connecting ? "Connecting..." : "Connect & Continue"}
              </button>
              <button
                onClick={() => {
                  setShowDbModal(false);
                  setSelectedDb(null);
                }}
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
      )}
    </div>
  );
}
