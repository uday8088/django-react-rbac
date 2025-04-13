// In VS Code, create a new file at frontend/app/login/page.tsx
"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"

export default function LoginPage() {
  const router = useRouter()
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")

  const handleLogin = (e: React.FormEvent) => {
    e.preventDefault()

    // In a real app, this would be an API call to your Django backend
    if (username === "admin" && password === "admin") {
      // Simulate admin login
      localStorage.setItem(
        "user",
        JSON.stringify({
          id: 1,
          username: "admin",
          role: "Admin",
        })
      )
      router.push("/dashboard")
    } else if (username === "user" && password === "user") {
      // Simulate regular user login
      localStorage.setItem(
        "user",
        JSON.stringify({
          id: 2,
          username: "user",
          role: "User",
        })
      )
      router.push("/dashboard")
    } else {
      alert("Invalid credentials. Try admin/admin or user/user")
    }
  }

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-50">
      <Card className="w-full max-w-md">
        <CardHeader>
          <CardTitle>Login</CardTitle>
          <CardDescription>Enter your credentials to access the dashboard</CardDescription>
        </CardHeader>
        <form onSubmit={handleLogin}>
          <CardContent className="space-y-4">
            <div className="space-y-2">
              <label htmlFor="username" className="text-sm font-medium">Username</label>
              <input
                id="username"
                className="w-full p-2 border rounded-md"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Username"
                required
              />
            </div>
            <div className="space-y-2">
              <label htmlFor="password" className="text-sm font-medium">Password</label>
              <input
                id="password"
                type="password"
                className="w-full p-2 border rounded-md"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                placeholder="Password"
                required
              />
            </div>
            <div className="text-sm text-gray-500">
              Demo accounts:
              <ul className="list-disc list-inside mt-1">
                <li>Admin: username: admin, password: admin</li>
                <li>User: username: user, password: user</li>
              </ul>
            </div>
          </CardContent>
          <CardFooter>
            <Button type="submit" className="w-full">
              Login
            </Button>
          </CardFooter>
        </form>
      </Card>
    </div>
  )
}