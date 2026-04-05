import React from "react";
import { Navbar } from "@/components/Navbar";
import { Button } from "@/components/ui/Button";
import { Card } from "@/components/ui/Card";
import { StatusBadge } from "@/components/ui/StatusBadge";

export default function Home() {
  return (
    <div className="bg-surface text-foreground selection:bg-secondary selection:text-foreground">
      <Navbar />

      <main className="max-w-[1400px] mx-auto px-12 py-12">
        {/* Hero Section */}
        <div className="flex justify-between items-start mb-12">
          <div>
            <p className="text-[10px] uppercase tracking-widest font-bold text-foreground/40 mb-2">
              Ghost Inventory Dashboard
            </p>
            <h1 className="text-8xl font-black tracking-tighter text-primary leading-none mb-6">
              $12,480.00
            </h1>
            <p className="text-xl text-foreground/40 max-w-md leading-relaxed">
              Value Locked in inactive personal assets. Ready for circular redistribution.
            </p>
          </div>
          <Button variant="secondary" size="lg" className="mt-8 flex items-center gap-2">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M13 10V3L4 14h7v7l9-11h-7z" /></svg>
            START AUDIT
          </Button>
        </div>

        {/* Intelligence Banner */}
        <div className="relative w-full h-48 rounded-md bg-gradient-to-br from-primary to-primary-accent overflow-hidden mb-16 flex items-center justify-center text-center">
          {/* Simple Graphic Patterns */}
          <div className="absolute inset-0 opacity-10">
            <div className="absolute top-0 right-0 w-64 h-64 bg-white rounded-full -translate-y-1/2 translate-x-1/3"></div>
            <div className="absolute bottom-0 left-0 w-48 h-48 bg-white rounded-full translate-y-1/2 -translate-x-1/3"></div>
          </div>

          <div className="relative z-10">
            <h2 className="text-3xl font-bold text-white mb-2">Intelligence Engine Active</h2>
            <p className="text-white/60 text-sm">Scanning 42 connected digital platforms for circular opportunities</p>
          </div>

          {/* Scan Beam */}
          <div className="absolute top-0 bottom-0 w-1/4 bg-white/10 animate-scan pointer-events-none"></div>
        </div>

        {/* Dashboard Grid */}
        <div className="flex gap-12">
          {/* Main Content: Detected Inventory */}
          <div className="flex-1">
            <div className="flex items-center justify-between mb-8">
              <div className="flex items-center gap-3">
                <h3 className="text-2xl font-bold tracking-tight">Detected Inventory</h3>
                <span className="px-2 py-0.5 bg-surface-low rounded-sm text-[10px] font-bold text-foreground/40">24 ITEMS</span>
              </div>
              <div className="flex items-center gap-2 bg-surface-low p-1 rounded-sm">
                <button className="p-1.5 bg-white shadow-sm rounded-xs"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M3 3h7v7H3V3zm11 0h7v7h-7V3zm0 11h7v7h-7v-7zm-11 0h7v7H3v-7z" /></svg></button>
                <button className="p-1.5 text-foreground/30 hover:text-foreground"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M4 6h16v2H4V6zm0 5h16v2H4v-2zm0 5h16v2H4v-2z" /></svg></button>
              </div>
            </div>

            <div className="grid grid-cols-2 gap-6">
              <InventoryCard
                title="Arc'teryx Alpha SV"
                category="Apparel"
                bought="2023"
                resale="$245"
                health={88}
                image="https://api.dicebear.com/7.x/identicon/svg?seed=arc"
              />
              <InventoryCard
                title='iPad Pro 12.9" M2'
                category="Tech"
                bought="2022"
                resale="$680"
                health={62}
                image="https://api.dicebear.com/7.x/identicon/svg?seed=ipad"
              />
              <InventoryCard
                title="Uniqlo Down Parka"
                category="Apparel"
                bought="2021"
                resale="$110"
                health={41}
                image="https://api.dicebear.com/7.x/identicon/svg?seed=uniqlo"
              />
            </div>
          </div>

          {/* Sidebar */}
          <aside className="w-80 space-y-12">
            <div>
              <div className="flex items-center gap-2 text-primary font-bold mb-6">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z" /></svg>
                <h4 className="text-sm tracking-tight">Intelligence Feed</h4>
              </div>
              <div className="space-y-8 relative">
                <div className="absolute left-1.5 top-2 bottom-2 w-0.5 bg-surface-low"></div>
                <FeedItem
                  source="GMAIL CONNECTOR"
                  message="New receipt detected: Peak Design Travel Backpack"
                  time="JUST NOW"
                  status="SYSTEM SYNC"
                />
                <FeedItem
                  source="MARKET INTELLIGENCE"
                  message="Resale value for 'iPhone 13' increased by 4.2%"
                  time="2 HOURS AGO"
                />
                <FeedItem
                  source="AMAZON SYNC"
                  message="Order #9924 verified: Sony WH-1000XM5"
                  time="YESTERDAY"
                />
              </div>
              <Button variant="ghost" size="sm" className="w-full mt-8 border border-outline-variant/15 text-foreground/40">
                VIEW FULL HISTORY
              </Button>
            </div>

            <Card className="bg-primary text-white p-8 relative overflow-hidden">
              <div className="absolute top-0 right-0 w-32 h-32 bg-white/10 rounded-full translate-x-1/3 -translate-y-1/3 blur-xl"></div>
              <h4 className="text-xl font-bold mb-4 relative z-10">Circular Impact</h4>
              <p className="text-white/60 text-sm mb-8 relative z-10">By redistributing your ghost inventory, you could offset 420kg of CO2 this year.</p>
              <button className="flex items-center gap-2 text-secondary font-bold text-xs group relative z-10">
                EXPLORE POTENTIAL
                <svg className="group-hover:translate-x-1 transition-transform" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"><path d="M5 12h14m-7-7 7 7-7 7" /></svg>
              </button>
            </Card>
          </aside>
        </div>
      </main>
    </div>
  );
}

function InventoryCard({ title, category, bought, resale, health, image }: any) {
  return (
    <Card className="group relative" hover>
      <div className="relative aspect-square bg-surface-low rounded-xs mb-6 overflow-hidden flex items-center justify-center p-8">
        <img src={image} alt={title} className="w-full h-full object-contain opacity-80 group-hover:scale-105 transition-transform duration-500" />
        <div className="absolute top-3 right-3 px-3 py-1 bg-white shadow-sm rounded-full text-[10px] font-bold text-primary">
          EST. RESALE: {resale}
        </div>
      </div>

      <div className="mb-4">
        <div className="flex items-center justify-between">
          <h5 className="text-lg font-bold tracking-tight">{title}</h5>
          <button className="text-foreground/20 hover:text-foreground">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="1" /><circle cx="19" cy="12" r="1" /><circle cx="5" cy="12" r="1" /></svg>
          </button>
        </div>
        <p className="text-[10px] uppercase tracking-widest font-bold text-foreground/30">
          {category} • BOUGHT {bought}
        </p>
      </div>

      <div className="mb-8">
        <div className="flex items-center justify-between mb-1.5">
          <span className="text-[10px] font-bold text-foreground/40">SUSTAINABILITY HEALTH</span>
          <span className="text-[10px] font-bold text-secondary">{health}%</span>
        </div>
        <div className="w-full h-1 bg-surface-low rounded-full overflow-hidden">
          <div className="h-full bg-secondary" style={{ width: `${health}%` }}></div>
        </div>
      </div>

      <div className="flex gap-3">
        <Button variant="ghost" size="sm" className="flex-1 bg-surface-low/50 border border-outline-variant/10 text-[10px]">
          {category === "Tech" ? "RECYCLE" : "LIST FOR SALE"}
        </Button>
        <Button variant="ghost" size="sm" className="flex-1 bg-surface-low/50 border border-outline-variant/10 text-[10px]">
          {category === "Tech" ? "TRADE-IN" : "VIEW LCA"}
        </Button>
      </div>
    </Card>
  );
}

function FeedItem({ source, message, time, status }: any) {
  return (
    <div className="pl-6 relative">
      <div className="absolute left-0 top-1.5 w-3 h-3 rounded-full bg-secondary border-4 border-surface "></div>
      <p className="text-[10px] font-black text-primary tracking-wider mb-1 leading-none">{source}</p>
      <p className="text-xs font-medium text-foreground tracking-tight leading-tight mb-1">{message}</p>
      <div className="flex items-center gap-2">
        <span className="text-[9px] font-bold text-foreground/20">{time}</span>
        {status && (
          <>
            <span className="text-[9px] text-foreground/10">•</span>
            <span className="text-[9px] font-bold text-foreground/20 uppercase tracking-widest">{status}</span>
          </>
        )}
      </div>
    </div>
  );
}
