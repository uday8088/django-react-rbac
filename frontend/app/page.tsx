// In VS Code, edit frontend/app/page.tsx
import Link from "next/link"
import { Button } from "@/components/ui/button"

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8 text-center">
      <h1 className="text-4xl font-bold mb-6">Role-Based Access Control Demo</h1>
      <p className="text-xl mb-8 max-w-2xl">
        A full-stack application demonstrating role-based menu access with Django, PostgreSQL, and React
      </p>
      <div className="flex gap-4">
        <Button asChild>
          <Link href="/login">Login Demo</Link>
        </Button>
        <Button variant="outline" asChild>
          <Link href="https://github.com/yourusername/django-react-rbac" target="_blank">
            View Source
          </Link>
        </Button>
      </div>
    </div>
  )
}