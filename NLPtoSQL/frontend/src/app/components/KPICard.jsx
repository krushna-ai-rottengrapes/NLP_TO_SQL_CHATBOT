"use client";

export default function KPICard({ label, value }) {
  const formatLabel = (text) => {
    return text.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
  };

  return (
    <div className="rounded-lg border border-gray-200 bg-white p-6 shadow-sm transition-all hover:shadow-md hover:shadow-blue-200 dark:border-gray-700 dark:bg-gray-900 dark:hover:shadow-blue-900">
      <p className="text-sm font-medium text-gray-600 dark:text-gray-400 truncate" title={formatLabel(label)}>
        {formatLabel(label)}
      </p>
      <p className="mt-2 text-3xl font-bold text-gray-900 dark:text-white truncate">
        {typeof value === "number" ? value.toLocaleString() : value}
      </p>
    </div>
  );
}
