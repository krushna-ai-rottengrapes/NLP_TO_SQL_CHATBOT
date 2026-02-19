"use client";

import {
  Moon,
  Sun,
  LogOut,
  LogIn,
  Database,
  LayoutDashboard,
  ArrowLeft,
  Save,
} from "lucide-react";
import { useContext } from "react";
import { useRouter, usePathname } from "next/navigation";
import { ThemeContext } from "../ThemeContext";
import { useAuth } from "../contexts/AuthContext";

export default function Navbar({
  onSaveDashboard,
  databaseName,
  dashboardTitle,
  isExisting,
}) {
  const { isDark, toggleTheme, mounted } = useContext(ThemeContext);
  const { user, logout } = useAuth();
  // console.log("Navbar user:", user);
  const router = useRouter();
  const pathname = usePathname();

  const isStudioPage = pathname === "/studio";

  const handleLogout = async () => {
    await logout();
    router.push("/login");
  };

  if (!mounted) return null;

  return (
    <nav
      className={`sticky top-0 z-50 border-b shadow-sm ${
        isDark ? "border-gray-800 bg-gray-950" : "border-gray-200 bg-white"
      }`}
    >
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4 sm:px-6 lg:px-8">
        <div className="flex items-center gap-4">
          {isStudioPage && user ? (
            <>
              <button
                onClick={() => router.push("/dashboard")}
                className={`flex items-center gap-2 rounded-lg px-3 py-2 transition-colors ${
                  isDark
                    ? "text-gray-400 hover:bg-gray-800"
                    : "text-gray-600 hover:bg-gray-100"
                }`}
                title="Back to Dashboard"
              >
                <ArrowLeft size={20} />
                <span className="text-sm font-medium">Back</span>
              </button>
              <div className="flex items-center gap-3">
                <div className="flex items-center gap-2">
                  <Database className="text-blue-600" size={20} />
                  <span
                    className={`text-sm font-medium ${
                      isDark ? "text-white" : "text-gray-900"
                    }`}
                  >
                    {databaseName || "Connected Database"}
                  </span>
                </div>
                {dashboardTitle && (
                  <>
                    <span
                      className={isDark ? "text-gray-600" : "text-gray-400"}
                    >
                      |
                    </span>
                    <span
                      className={`text-sm font-medium ${
                        isDark ? "text-gray-300" : "text-gray-700"
                      }`}
                    >
                      {dashboardTitle}
                    </span>
                  </>
                )}
              </div>
            </>
          ) : (
            <div
              className={`text-xl font-semibold ${
                isDark ? "text-white" : "text-gray-900"
              }`}
            >
              NLP → SQL Studio
            </div>
          )}
        </div>

        <div className="flex items-center gap-4">
          {user && (
            <>
              {isStudioPage ? (
                <>
                  {onSaveDashboard && (
                    <button
                      onClick={onSaveDashboard}
                      className="flex items-center gap-2 rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
                      title={isExisting ? "Save Changes" : "Save Dashboard"}
                    >
                      <Save size={18} />
                      <span className="text-sm font-medium">
                        {isExisting ? "Save Changes" : "Save Dashboard"}
                      </span>
                    </button>
                  )}
                </>
              ) : (
                <>
                  <button
                    onClick={() => router.push("/dashboard")}
                    className={`rounded-lg p-2 transition-colors ${
                      isDark
                        ? "text-gray-400 hover:bg-gray-800"
                        : "text-gray-600 hover:bg-gray-100"
                    }`}
                    title="Dashboards"
                  >
                    <LayoutDashboard size={20} />
                  </button>
                  <button
                    onClick={() => router.push("/connections")}
                    className={`rounded-lg p-2 transition-colors ${
                      isDark
                        ? "text-gray-400 hover:bg-gray-800"
                        : "text-gray-600 hover:bg-gray-100"
                    }`}
                    title="Connections"
                  >
                    <Database size={20} />
                  </button>
                </>
              )}
            </>
          )}

          <button
            onClick={toggleTheme}
            className={`rounded-lg p-2 transition-colors ${
              isDark
                ? "text-yellow-400 hover:bg-gray-800"
                : "text-gray-600 hover:bg-gray-100"
            }`}
            aria-label="Toggle theme"
          >
            {isDark ? <Sun size={20} /> : <Moon size={20} />}
          </button>

          {user ? (
            <button
              onClick={handleLogout}
              className={`rounded-lg p-2 transition-colors ${
                isDark
                  ? "text-red-400 hover:bg-gray-800"
                  : "text-red-600 hover:bg-gray-100"
              }`}
              title="Logout"
            >
              <LogOut size={20} />
            </button>
          ) : (
            <button
              onClick={() => window.location.href = "/login"}
              className={`rounded-lg p-2 transition-colors ${
                isDark
                  ? "text-green-400 hover:bg-gray-800"
                  : "text-green-600 hover:bg-gray-100"
              }`}
              title="Login"
            >
              <LogIn size={20} />
            </button>
          )}
        </div>
      </div>
    </nav>
  );
}
