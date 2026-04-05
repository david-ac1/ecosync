import React from "react";
import Link from "next/link";
import { StatusBadge } from "./ui/StatusBadge";

export const Navbar = () => {
    return (
        <nav className="sticky top-0 z-50 glass border-b border-outline-variant/15 px-8 h-20 flex items-center justify-between">
            <div className="flex items-center gap-12">
                <Link href="/" className="text-2xl font-black text-primary tracking-tighter">
                    EcoSync
                </Link>
                <div className="flex items-center gap-8 text-sm font-medium text-foreground/60">
                    <Link href="#" className="text-primary border-b-2 border-primary pb-1">Intelligence</Link>
                    <Link href="#" className="hover:text-foreground transition-colors">Circular Assets</Link>
                    <Link href="#" className="hover:text-foreground transition-colors">Supply Chain</Link>
                </div>
            </div>

            <div className="flex items-center gap-6">
                <StatusBadge label="Agent Status" />
                <div className="flex items-center gap-3">
                    <div className="text-primary">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M2 8c.722 0 1.434.144 2.1.424m15.8.001c.666-.28 1.378-.425 2.1-.425M5 12c.534 0 1.057.116 1.54.34M17.46 12.34c.483-.224 1.006-.34 1.54-.34M8 16c.382 0 .755.093 1.1.272m5.8.001A2.24 2.24 0 0 1 16 16M12 12v.01" /></svg>
                    </div>
                    <div className="w-10 h-10 rounded-full bg-surface-low overflow-hidden border border-outline-variant/15">
                        <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Felix" alt="User" />
                    </div>
                </div>
            </div>
        </nav>
    );
};
