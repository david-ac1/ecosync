import React from "react";

interface CardProps {
    children: React.ReactNode;
    className?: string;
    variant?: "default" | "low" | "lowest";
    hover?: boolean;
}

export const Card = ({
    children,
    className = "",
    variant = "lowest",
    hover = false,
}: CardProps) => {
    const variants = {
        default: "bg-surface",
        low: "bg-surface-low",
        lowest: "bg-surface-lowest",
    };

    const hoverStyles = hover ? "hover:shadow-ambient transition-shadow duration-300" : "";

    return (
        <div className={`rounded-md p-6 ${variants[variant]} ${hoverStyles} ${className}`}>
            {children}
        </div>
    );
};
