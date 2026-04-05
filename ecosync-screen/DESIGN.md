# Design System Specification: Circular Intelligence

## 1. Overview & Creative North Star
### The Creative North Star: "The Digital Architect"
This design system moves beyond the generic "SaaS aesthetic" to establish a visual language rooted in **High-Tech Intentionality.** It rejects the cluttered complexity of traditional enterprise software in favor of an editorial-grade experience that feels both authoritative and hyper-modern. 

The system leverages **Intentional Asymmetry** and **Aggressive Whitespace** to guide the user’s eye. We are not just building a platform; we are building a blueprint for the circular economy. The interface should feel like a premium physical object—think matte-finish aluminum meets high-density frosted glass. We break the grid by overlapping high-contrast typography over soft, layered surfaces, creating a sense of three-dimensional depth in a strictly 2D vector world.

---

## 2. Colors & Surface Logic
The palette is a high-contrast dialogue between the deep, intellectual weight of Indigo and the kinetic energy of Fluorescent Lime.

### The Color Roles
*   **Primary (#3525CD / #4F46E5):** Our "Logic" color. Used for deep-focus areas and primary actions.
*   **Secondary (#556500 / #D9FF00):** Our "Kinetic" accent. Use this sparingly to highlight critical data points or "Positive Impact" metrics.
*   **Neutral (Surface Tiers):** A range of cool greys that define our spatial architecture.

### The "No-Line" Rule
**Explicit Instruction:** Use of 1px solid borders for sectioning is strictly prohibited. 
In this design system, boundaries are defined through **Background Color Shifts**. To separate a sidebar from a main feed, use a shift from `surface` (#F8F9FA) to `surface-container-low` (#F3F4F5). This creates a sophisticated, seamless transition that feels architectural rather than "boxed in."

### Glassmorphism & Tonal Gradients
To avoid a flat, "out-of-the-box" look, use semi-transparent `surface` colors with a `backdrop-blur` (min 20px) for floating navigation bars or contextual overlays.
*   **Signature Textures:** For Hero sections, utilize a subtle linear gradient from `primary` (#3525CD) to `primary_container` (#4F46E5) at a 135-degree angle. This adds "visual soul" and movement to the background.

---

## 3. Typography: The Editorial Edge
We utilize **Inter** not as a functional workhorse, but as a bold, geometric statement.

*   **Display (Display-LG/MD):** These are your "Editorial Anchors." Use negative letter-spacing (-0.02em) and bold weights. They should feel massive, commanding the page.
*   **Headlines & Titles:** Used to categorize data. Always pair a `headline-lg` with a `body-md` to create a high-contrast hierarchy that mimics a premium broadsheet.
*   **Labels (Label-SM):** All-caps with increased letter-spacing (+0.05em) for metadata or small tags.

The typography is the primary driver of brand authority. If a layout feels "weak," increase the type scale contrast rather than adding decorative elements.

---

## 4. Elevation & Depth: Tonal Layering
We do not use structural lines; we use **Stacking Logic.**

*   **The Layering Principle:** Depth is achieved by nesting surface tokens. 
    *   *Base Layer:* `surface` (#F8F9FA)
    *   *Section Layer:* `surface-container-low` (#F3F4F5)
    *   *Interactive Card:* `surface-container-lowest` (#FFFFFF)
*   **Ambient Shadows:** For "Floating" elements (like Tooltips or floating FABs), use an extra-diffused shadow:
    *   `box-shadow: 0 20px 40px rgba(77, 68, 227, 0.06);` 
    *   Note: The shadow color is a tinted Indigo, not grey, to maintain vibrancy.
*   **The "Ghost Border" Fallback:** If a container requires more definition on a white background, use `outline-variant` (#C7C4D8) at **15% opacity**. It should be felt, not seen.

---

## 5. Components

### Buttons
*   **Primary:** Pill-shaped (`rounded-full`), `primary` background with `on-primary` text. No shadow on rest; a subtle "glow" (diffused primary color shadow) on hover.
*   **Accent/Action:** Pill-shaped, `secondary_fixed` (#CDF200) background. Reserved for high-conversion circular economy actions (e.g., "Start Audit").

### Cards
*   **Geometry:** 16px (`DEFAULT`) or 24px (`md`) rounded corners.
*   **Styling:** Forbid dividers. Separate internal content using 32px of vertical padding or a `surface-variant` background for the card footer.

### Inputs
*   **Visual Style:** Soft-filled `surface-container-high` backgrounds. No borders. On focus, a 2px `primary` underline or a subtle `surface-tint` glow. 
*   **Labels:** Floating labels using `label-md` for a tech-forward, minimal footprint.

### Data Visualizations (Specialty)
*   As a platform for circular intelligence, use the **Fluorescent Lime** for growth/positive metrics and **Electric Indigo** for baseline/stable data. Use thick, 4px stroke widths for charts to match the bold typography.

---

## 6. Do's and Don'ts

### Do:
*   **Do** use asymmetrical layouts where text blocks and illustrations overlap slightly to create depth.
*   **Do** embrace massive amounts of whitespace—if you think it's too much, add 16px more.
*   **Do** use the "Pill" shape for all interactive triggers to maintain a friendly, modern high-tech feel.
*   **Do** ensure all text on Indigo backgrounds uses the `on_primary` (#FFFFFF) token for WCAG 2.2 AA compliance.

### Don't:
*   **Don't** use 1px black or grey borders. They break the premium "architectural" feel.
*   **Don't** use standard "drop shadows" (e.g., `rgba(0,0,0,0.5)`). Use the tinted Ambient Shadow logic.
*   **Don't** use the Fluorescent Lime (#D9FF00) for body text; it is strictly for accents, highlights, and secondary CTAs.
*   **Don't** use sharp 90-degree corners. Everything must feel approachable through the `1rem` to `full` roundedness scale.