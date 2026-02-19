"use client";

import {
  useReactTable,
  getCoreRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  getFilteredRowModel,
  flexRender,
} from "@tanstack/react-table";
import { useState, useMemo, useContext } from "react";
import { ChevronUp, ChevronDown, Download } from "lucide-react";
import Papa from "papaparse";
import { ThemeContext } from "../ThemeContext";

export default function DataTable({ columns: columnNames, data }) {
  const { isDark } = useContext(ThemeContext);
  const [sorting, setSorting] = useState([]);
  const [globalFilter, setGlobalFilter] = useState("");
  const [pagination, setPagination] = useState({ pageIndex: 0, pageSize: 10 });

  const columns = useMemo(
    () =>
      columnNames.map((name) => ({
        accessorKey: name,
        header: name,
        cell: (info) => {
          const value = info.getValue();
          return typeof value === "object" ? JSON.stringify(value) : String(value);
        },
      })),
    [columnNames]
  );

  const table = useReactTable({
    data,
    columns,
    state: { sorting, globalFilter, pagination },
    onSortingChange: setSorting,
    onGlobalFilterChange: setGlobalFilter,
    onPaginationChange: setPagination,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getFilteredRowModel: getFilteredRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
  });

  const downloadCSV = () => {
    const csv = Papa.unparse({
      fields: columnNames,
      data: data.map((row) => columnNames.map((col) => row[col])),
    });
    const blob = new Blob([csv], { type: "text/csv" });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "results.csv";
    a.click();
  };

  return (
    <div className="space-y-4">
      <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
        <input
          type="text"
          placeholder="Search..."
          value={globalFilter}
          onChange={(e) => setGlobalFilter(e.target.value)}
          className={`rounded-lg border px-3 py-2 text-sm placeholder-gray-500 focus:border-blue-500 focus:outline-none ${
            isDark
              ? "border-gray-600 bg-gray-900 text-white"
              : "border-gray-300 bg-white text-gray-900"
          }`}
        />
        <button
          onClick={downloadCSV}
          className={`flex items-center gap-2 rounded-lg px-3 py-2 text-sm font-medium text-white transition-colors ${
            isDark
              ? "bg-green-700 hover:bg-green-800"
              : "bg-green-600 hover:bg-green-700"
          }`}
        >
          <Download size={16} />
          CSV
        </button>
      </div>

      <div
        className={`overflow-x-auto rounded-lg border ${
          isDark ? "border-gray-700" : "border-gray-200"
        }`}
      >
        <table className="w-full text-sm">
          <thead
            className={`sticky top-0 border-b ${
              isDark
                ? "border-gray-700 bg-gray-900"
                : "border-gray-200 bg-gray-50"
            }`}
          >
            {table.getHeaderGroups().map((headerGroup) => (
              <tr key={headerGroup.id}>
                {headerGroup.headers.map((header) => (
                  <th
                    key={header.id}
                    className={`px-4 py-3 text-left font-semibold ${
                      isDark ? "text-gray-300" : "text-gray-700"
                    }`}
                  >
                    <button
                      onClick={header.column.getToggleSortingHandler()}
                      className={`flex items-center gap-2 ${
                        isDark
                          ? "hover:text-white"
                          : "hover:text-gray-900"
                      }`}
                    >
                      {flexRender(
                        header.column.columnDef.header,
                        header.getContext()
                      )}
                      {header.column.getIsSorted() && (
                        <>
                          {header.column.getIsSorted() === "asc" ? (
                            <ChevronUp size={14} />
                          ) : (
                            <ChevronDown size={14} />
                          )}
                        </>
                      )}
                    </button>
                  </th>
                ))}
              </tr>
            ))}
          </thead>
          <tbody>
            {table.getRowModel().rows.map((row) => (
              <tr
                key={row.id}
                className={`border-b ${
                  isDark
                    ? "border-gray-700 hover:bg-gray-900"
                    : "border-gray-200 hover:bg-gray-50"
                }`}
              >
                {row.getVisibleCells().map((cell) => (
                  <td
                    key={cell.id}
                    className={`px-4 py-3 ${
                      isDark ? "text-gray-100" : "text-gray-900"
                    }`}
                  >
                    {flexRender(cell.column.columnDef.cell, cell.getContext())}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="flex flex-col items-center justify-between gap-3 sm:flex-row">
        <div
          className={`text-sm ${
            isDark ? "text-gray-400" : "text-gray-600"
          }`}
        >
          Page {table.getState().pagination.pageIndex + 1} of{" "}
          {table.getPageCount()}
        </div>
        <div className="flex gap-2">
          <button
            onClick={() => table.previousPage()}
            disabled={!table.getCanPreviousPage()}
            className={`rounded-lg border px-3 py-2 text-sm font-medium disabled:opacity-50 ${
              isDark
                ? "border-gray-600 text-gray-300 hover:bg-gray-900"
                : "border-gray-300 text-gray-900 hover:bg-gray-50"
            }`}
          >
            Previous
          </button>
          <button
            onClick={() => table.nextPage()}
            disabled={!table.getCanNextPage()}
            className={`rounded-lg border px-3 py-2 text-sm font-medium disabled:opacity-50 ${
              isDark
                ? "border-gray-600 text-gray-300 hover:bg-gray-900"
                : "border-gray-300 text-gray-900 hover:bg-gray-50"
            }`}
          >
            Next
          </button>
        </div>
      </div>
    </div>
  );
}
