"use client";

import { Doughnut } from "react-chartjs-2";
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from "chart.js";

ChartJS.register(ArcElement, Tooltip, Legend);

export default function DoughnutChart({ data, isDark }) {
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: "right", labels: { color: isDark ? "#e5e7eb" : "#374151" } },
    },
  };

  return (
    <div className="h-full w-full">
      <Doughnut data={data} options={options} />
    </div>
  );
}
