"use client";

import { useState, useEffect, useContext } from "react";
import { Loader, MessageCircle, X } from "lucide-react";
import DataTable from "./DataTable";
import KPICard from "./KPICard";
import { useApi } from "../hooks/useApi";
import { ThemeContext } from "../ThemeContext";

export default function ResultPanel({ sqlQuery, onResultData }) {
  const { isDark } = useContext(ThemeContext);
  const [result, setResult] = useState(null);
  const [localLoading, setLocalLoading] = useState(false);
  const [showModal, setShowModal] = useState(false);
  const { executeSql, error } = useApi();

  useEffect(() => {
    if (!sqlQuery) {
      return;
    }

    // Check if query is a read-only warning message
    if (
      sqlQuery.includes("I can only generate SELECT queries") ||
      sqlQuery.includes("cannot modify the database")
    ) {
      setResult(null);
      return;
    }

    const execute = async () => {
      setLocalLoading(true);
      try {
        const res = await executeSql(sqlQuery);
        setResult(res);
        if (onResultData) {
          onResultData(res);
        }
      } catch (err) {
        console.error("Execution error:", err);
      } finally {
        setLocalLoading(false);
      }
    };

    execute();
  }, [sqlQuery, executeSql]);

  const renderContent = () => {
    if (!result?.data || result.data.length === 0) return null;

    const rowCount = result.data.length;

    // Multiple rows: show as table
    if (rowCount > 1) {
      return <DataTable columns={result.columns} data={result.data} />;
    }

    // Single row: use backend segregation
    const cards = result.cards || [];
    const tables = result.tables || [];
    const entries = Object.entries(result.data[0]);

    // If only 1 field and it's scalar, show as card
    if (entries.length === 1 && cards.length === 0 && tables.length === 0) {
      const [key, value] = entries[0];
      if (!Array.isArray(value)) {
        cards.push({ label: key, value });
      }
    }

    return (
      <>
        {cards.length > 0 && (
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-2 mb-6">
            {cards.map((card) => (
              <KPICard key={card.label} label={card.label} value={card.value} />
            ))}
          </div>
        )}

        {tables.length > 0 && (
          <div className="space-y-6">
            {tables.map((table) => (
              <div key={table.name}>
                <h3
                  className={`text-sm font-semibold mb-3 ${
                    isDark ? "text-gray-300" : "text-gray-700"
                  }`}
                >
                  {table.name
                    .replace(/_/g, " ")
                    .replace(/\b\w/g, (c) => c.toUpperCase())}
                </h3>
                <DataTable
                  columns={
                    table.data.length > 0 ? Object.keys(table.data[0]) : []
                  }
                  data={table.data}
                />
              </div>
            ))}
          </div>
        )}

        {cards.length === 0 &&
          tables.length === 0 &&
          Object.entries(result.data[0]).length > 1 && (
            <DataTable columns={result.columns} data={result.data} />
          )}
      </>
    );
  };

  return (
    <div
      className={`h-full overflow-auto ${isDark ? "bg-gray-950" : "bg-white"}`}
    >
      {!sqlQuery && (
        <div
          className={`flex h-full items-center justify-center ${
            isDark ? "text-gray-400" : "text-gray-500"
          }`}
        >
          <p>Select a SQL query to see results</p>
        </div>
      )}

      {sqlQuery && localLoading && (
        <div className="flex h-full items-center justify-center">
          <div className="flex flex-col items-center gap-3">
            <Loader className="animate-spin text-blue-600" size={32} />
            <p
              className={`text-sm ${
                isDark ? "text-gray-400" : "text-gray-600"
              }`}
            >
              Executing query...
            </p>
          </div>
        </div>
      )}

      {sqlQuery && error && (
        <div className="flex h-full items-center justify-center">
          <div
            className={`rounded-lg border p-4 ${
              isDark ? "border-red-900 bg-red-950" : "border-red-200 bg-red-50"
            }`}
          >
            <p
              className={`text-sm font-medium ${
                isDark ? "text-red-200" : "text-red-800"
              }`}
            >
              Error: {error}
            </p>
          </div>
        </div>
      )}

      {sqlQuery && !localLoading && !error && result && (
        <div className="p-4 sm:p-6">
          {renderContent()}

          <button
            onClick={() => setShowModal(true)}
            className="fixed bottom-6 right-6 flex h-14 w-14 items-center justify-center rounded-full bg-blue-600 text-white shadow-lg transition-all hover:bg-blue-700 hover:shadow-xl"
            title="Talk to Data"
          >
            <MessageCircle size={24} />
          </button>

          {showModal && (
            <div className="fixed inset-0 z-50 flex items-end justify-end p-4 sm:items-center sm:justify-center">
              <div
                className="fixed inset-0 bg-black/50"
                onClick={() => setShowModal(false)}
              />
              <div
                className={`relative z-50 w-full max-w-sm rounded-lg p-6 shadow-xl ${
                  isDark ? "bg-gray-900" : "bg-white"
                }`}
              >
                <button
                  onClick={() => setShowModal(false)}
                  className={`absolute top-4 right-4 ${
                    isDark
                      ? "text-gray-400 hover:text-gray-200"
                      : "text-gray-500 hover:text-gray-700"
                  }`}
                >
                  <X size={20} />
                </button>
                <h3
                  className={`text-lg font-semibold ${
                    isDark ? "text-white" : "text-gray-900"
                  }`}
                >
                  Talk to Data
                </h3>
                <p
                  className={`mt-2 text-sm ${
                    isDark ? "text-gray-400" : "text-gray-600"
                  }`}
                >
                  Coming soon
                </p>
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
