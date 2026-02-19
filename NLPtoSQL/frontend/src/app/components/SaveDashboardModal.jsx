"use client";

import { useState, useContext } from "react";
import { X } from "lucide-react";
import { ThemeContext } from "../ThemeContext";

export default function SaveDashboardModal({ isOpen, onClose, onSave, currentTitle = "" }) {
  const [title, setTitle] = useState(currentTitle);
  const { isDark } = useContext(ThemeContext);

  if (!isOpen) return null;

  const handleSubmit = (e) => {
    e.preventDefault();
    if (title.trim()) {
      onSave(title.trim());
      setTitle("");
    }
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50">
      <div className={`w-full max-w-md rounded-lg p-6 shadow-xl ${
        isDark ? "bg-gray-900" : "bg-white"
      }`}>
        <div className="mb-4 flex items-center justify-between">
          <h2 className={`text-xl font-semibold ${
            isDark ? "text-white" : "text-gray-900"
          }`}>
            Save Dashboard
          </h2>
          <button
            onClick={onClose}
            className={`rounded-lg p-1 transition-colors ${
              isDark ? "hover:bg-gray-800" : "hover:bg-gray-100"
            }`}
          >
            <X size={20} className={isDark ? "text-gray-400" : "text-gray-600"} />
          </button>
        </div>

        <form onSubmit={handleSubmit}>
          <div className="mb-4">
            <label className={`mb-2 block text-sm font-medium ${
              isDark ? "text-gray-300" : "text-gray-700"
            }`}>
              Dashboard Title
            </label>
            <input
              type="text"
              value={title}
              onChange={(e) => setTitle(e.target.value)}
              placeholder="Enter dashboard title..."
              className={`w-full rounded-lg border px-4 py-2 focus:outline-none focus:ring-2 focus:ring-blue-500 ${
                isDark
                  ? "border-gray-700 bg-gray-800 text-white placeholder-gray-500"
                  : "border-gray-300 bg-white text-gray-900 placeholder-gray-400"
              }`}
              autoFocus
            />
          </div>

          <div className="flex justify-end gap-3">
            <button
              type="button"
              onClick={onClose}
              className={`rounded-lg px-4 py-2 font-medium transition-colors ${
                isDark
                  ? "bg-gray-800 text-gray-300 hover:bg-gray-700"
                  : "bg-gray-200 text-gray-700 hover:bg-gray-300"
              }`}
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={!title.trim()}
              className="rounded-lg bg-blue-600 px-4 py-2 font-medium text-white transition-colors hover:bg-blue-700 disabled:cursor-not-allowed disabled:opacity-50"
            >
              Save
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
