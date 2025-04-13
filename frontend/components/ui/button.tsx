import * as React from "react"

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "default" | "outline"
  asChild?: boolean
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = "default", children, ...props }, ref) => {
    const baseStyles = "inline-flex items-center justify-center rounded-md px-4 py-2 text-sm font-medium"
    const variantStyles = variant === "default" 
      ? "bg-blue-600 text-white hover:bg-blue-700" 
      : "border border-gray-300 bg-white text-gray-700 hover:bg-gray-50"
    
    return (
      <button
        ref={ref}
        className={`${baseStyles} ${variantStyles} ${className || ""}`}
        {...props}
      >
        {children}
      </button>
    )
  }
)
Button.displayName = "Button"

export { Button }