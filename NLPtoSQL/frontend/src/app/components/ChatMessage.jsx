"use client";

import { Copy, Check } from "lucide-react";
import { useState, useContext } from "react";
import { ThemeContext } from "../ThemeContext";

export default function ChatMessage({ message, onReexecute }) {
  const { isDark } = useContext(ThemeContext);
  const [copied, setCopied] = useState(false);

  const copyToClipboard = () => {
    navigator.clipboard.writeText(message.sql_query);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const intentColors = {
    sql_query:
      "bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-200",
    casual_chat:
      "bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-200",
    sarcastic_response:
      "bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-200",
    ambiguous:
      "bg-orange-100 text-orange-800 dark:bg-orange-900 dark:text-orange-200",
  };

  return (
    <div className="space-y-3">
      {/* User message */}
      <div className="flex justify-end">
        <div className="max-w-[85%] rounded-lg bg-blue-600 px-4 py-2 text-white">
          <p className="text-sm break-words">{message.question}</p>
        </div>
      </div>

      {/* System response */}
      <div className="space-y-2">
        <div className="flex justify-start">
          <div className="w-full space-y-2">
            {/* Intent Badge */}
            <span
              className={`inline-block rounded-full px-3 py-1 text-xs font-semibold ${
                intentColors[message.intent] || intentColors.ambiguous
              }`}
            >
              {message.intent?.replace(/_/g, " ").toUpperCase()}
            </span>

            {/* SQL Query (only for sql_query intent) */}
            {message.intent === "sql_query" && message.sql_query && (
              <div
                className={`rounded-lg border p-3 ${
                  isDark
                    ? "border-gray-700 bg-gray-900"
                    : "border-gray-200 bg-gray-50"
                }`}
              >
                <div className="mb-2 flex items-center justify-between">
                  <span
                    className={`text-xs font-semibold ${
                      isDark ? "text-gray-400" : "text-gray-600"
                    }`}
                  >
                    SQL Query
                  </span>
                  <button
                    onClick={copyToClipboard}
                    className={`rounded p-1 ${
                      isDark
                        ? "text-gray-500 hover:bg-gray-800"
                        : "text-gray-500 hover:bg-gray-200"
                    }`}
                  >
                    {copied ? (
                      <Check size={16} className="text-green-600" />
                    ) : (
                      <Copy size={16} />
                    )}
                  </button>
                </div>
                <div className="overflow-x-auto rounded bg-gray-900 text-xs">
                  <pre
                    className={`m-0 p-3 text-xs ${
                      isDark ? "text-gray-300" : "text-gray-300"
                    }`}
                  >
                    <code>{message.sql_query}</code>
                  </pre>
                </div>
              </div>
            )}

            {/* Response Text (for non-SQL intents) */}
            {message.intent !== "sql_query" && message.response && (
              <div
                className={`rounded-lg border p-3 ${
                  isDark
                    ? "border-gray-700 bg-gray-900"
                    : "border-gray-200 bg-gray-50"
                }`}
              >
                <p
                  className={`text-sm ${
                    isDark ? "text-gray-300" : "text-gray-700"
                  }`}
                >
                  {message.response}
                </p>
              </div>
            )}

            {/* Tables Used */}
            {message.intent === "sql_query" &&
              message.filtered_tables &&
              message.filtered_tables.length > 0 && (
                <div className="flex flex-wrap gap-2">
                  {message.filtered_tables.map((table) => (
                    <span
                      key={table}
                      className={`inline-block rounded-full px-3 py-1 text-xs font-medium ${
                        isDark
                          ? "bg-purple-900 text-purple-200"
                          : "bg-purple-100 text-purple-700"
                      }`}
                    >
                      {table}
                    </span>
                  ))}
                </div>
              )}

            {/* Re-execute button (only for SQL) */}
            {message.intent === "sql_query" && onReexecute && (
              <button
                onClick={() => onReexecute(message)}
                className={`w-full rounded-lg px-3 py-2 text-xs font-medium text-white transition-colors ${
                  isDark
                    ? "bg-blue-700 hover:bg-blue-800"
                    : "bg-green-600 hover:bg-green-800"
                }`}
              >
                Re-execute Query
              </button>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
