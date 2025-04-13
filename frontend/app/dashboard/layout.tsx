"use client"

import { useEffect, useState } from "react"
import { useRouter } from "next/navigation"
import Link from "next/link"

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode
}) {
  const router = useRouter()
  const [user, setUser] = useState<any>(null)

  useEffect(() => {
    // Check if user is logged in
    const userData = localStorage.getItem("user")
    if (!userData) {
      router.push("/login")
      return
    }

    setUser(JSON.parse(userData))
  }, [router])

  const handleLogout = () => {
    localStorage.removeItem("user")
    router.push("/login")
  }

  if (!user) {
    return <div className="p-8">Loading...</div>
  }

  return (
    <div className="flex h-screen bg-gray-100">
      {/* Sidebar */}
      <div className="w-64 bg-white shadow-md">
        <div className="p-4 border-b">
          <h2 className="text-lg font-semibold">RBAC Demo</h2>
          <p className="text-sm text-gray-500">Role: {user.role}</p>
        </div>
        <nav className="p-4">
          <ul className="space-y-2">
            <li>
              <Link href="/dashboard" className="block p-2 rounded hover:bg-gray-100">
                Dashboard
              </Link>
            </li>
            {user.role === "Admin" && (
              <>
                <li>
                  <Link href="/dashboard/users" className="block p-2 rounded hover:bg-gray-100">
                    Users
                  </Link>
                </li>
                <li>
                  <Link href="/dashboard/roles" className="block p-2 rounded hover:bg-gray-100">
                    Roles
                  </Link>
                </li>
              </>
            )}
          </ul>
        </nav>
        <div className="p-4 border-t mt-auto">
          <button 
            onClick={handleLogout}
            className="w-full p-2 text-left text-red-600 hover:bg-gray-100 rounded"
          >
            Logout
          </button>
        </div>
      </div>
      
      {/* Main content */}
      <div className="flex-1 overflow-auto">
        <header className="bg-white shadow-sm p-4 border-b">
          <h1 className="text-xl font-semibold">Dashboard</h1>
        </header>
        <main className="p-4">
          {children}
        </main>
      </div>
    </div>
  )
}