"use client";

import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

export default function BarChart({ data, isDark }) {
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: "top", labels: { color: isDark ? "#e5e7eb" : "#374151" } },
    },
    scales: {
      x: { ticks: { color: isDark ? "#9ca3af" : "#6b7280" }, grid: { color: isDark ? "#374151" : "#e5e7eb" } },
      y: { ticks: { color: isDark ? "#9ca3af" : "#6b7280" }, grid: { color: isDark ? "#374151" : "#e5e7eb" } },
    },
  };

  return (
    <div className="h-full w-full">
      <Bar data={data} options={options} />
    </div>
  );
}
