import React from "react";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
    variant?: "primary" | "secondary" | "ghost";
    size?: "sm" | "md" | "lg";
}

export const Button = ({
    children,
    variant = "primary",
    size = "md",
    className = "",
    ...props
}: ButtonProps) => {
    const baseStyles = "rounded-full font-medium transition-all duration-300 flex items-center justify-center gap-2 cursor-pointer";

    const variants = {
        primary: "bg-primary text-white hover:shadow-ambient",
        secondary: "bg-secondary text-foreground hover:bg-secondary-accent",
        ghost: "bg-transparent text-foreground hover:bg-surface-low",
    };

    const sizes = {
        sm: "px-4 py-1.5 text-xs",
        md: "px-6 py-2.5 text-sm",
        lg: "px-8 py-3.5 text-base",
    };

    return (
        <button
            className={`${baseStyles} ${variants[variant]} ${sizes[size]} ${className}`}
            {...props}
        >
            {children}
        </button>
    );
};
