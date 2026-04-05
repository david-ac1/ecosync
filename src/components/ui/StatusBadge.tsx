import React from "react";

interface StatusBadgeProps {
    label: string;
    active?: boolean;
}

export const StatusBadge = ({ label, active = true }: StatusBadgeProps) => {
    return (
        <div className="flex items-center gap-2 px-3 py-1 bg-secondary/15 rounded-full">
            <div className={`w-2 h-2 rounded-full ${active ? "bg-secondary" : "bg-gray-400 animate-pulse"}`}></div>
            <span className="text-[10px] uppercase tracking-wider font-bold text-foreground/80">
                {label}
            </span>
        </div>
    );
};
