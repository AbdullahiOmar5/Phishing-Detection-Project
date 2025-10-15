import { Link, useLocation } from "react-router-dom";
import { Shield, Sun, Moon } from "lucide-react";
import { useEffect, useState } from "react";

type Theme = "light" | "dark";

export default function Header() {
  const location = useLocation();
  const [theme, setTheme] = useState<Theme>(() => {
    try {
      return (localStorage.getItem("theme") as Theme) || "light";
    } catch {
      return "light";
    }
  });

  useEffect(() => {
    // Apply theme class on document.documentElement
    const root = document.documentElement;
    root.classList.remove("dark");
    if (theme === "dark") root.classList.add("dark");
    try {
      localStorage.setItem("theme", theme);
    } catch {}
  }, [theme]);

  const isActive = (path: string) => location.pathname === path;

  return (
    <header className="sticky top-0 z-50 backdrop-blur-lg bg-white/70 dark:bg-gray-900/70 border-b border-gray-200 dark:border-gray-800 shadow-sm">
      <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          <Link to="/" className="flex items-center gap-2 group">
            <Shield className="w-8 h-8 text-blue-600 dark:text-blue-400 group-hover:scale-110 transition-transform" />
            <span className="text-xl font-bold bg-gradient-to-r from-blue-600 to-teal-600 dark:from-blue-400 dark:to-teal-400 bg-clip-text text-transparent">
              Phishing Detector
            </span>
          </Link>

          <div className="flex items-center gap-3">
            <div className="flex gap-1">
              <Link
                to="/"
                className={`px-4 py-2 rounded-lg font-medium transition-all ${
                  isActive("/")
                    ? "bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300"
                    : "text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800"
                }`}
              >
                Home
              </Link>
              <Link
                to="/predict"
                className={`px-4 py-2 rounded-lg font-medium transition-all ${
                  isActive("/predict")
                    ? "bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300"
                    : "text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800"
                }`}
              >
                Predict
              </Link>
              <Link
                to="/about"
                className={`px-4 py-2 rounded-lg font-medium transition-all ${
                  isActive("/about")
                    ? "bg-blue-100 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300"
                    : "text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800"
                }`}
              >
                About
              </Link>
            </div>

            {/* Theme selector */}
            <div className="flex items-center gap-2">
              <button
                onClick={() => setTheme(theme === "dark" ? "light" : "dark")}
                className={`p-2 rounded-md flex items-center justify-center transition-colors ${
                  theme === "dark"
                    ? "bg-gray-800 text-white"
                    : "bg-gray-100 text-gray-900"
                }`}
                title={
                  theme === "dark"
                    ? "Switch to light theme"
                    : "Switch to dark theme"
                }
              >
                {theme === "dark" ? (
                  <Moon className="w-5 h-5" />
                ) : (
                  <Sun className="w-5 h-5" />
                )}
              </button>
            </div>
          </div>
        </div>
      </nav>
    </header>
  );
}
