---
name: Clinical Clarity
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#414755'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005bc1'
  primary: '#0058bc'
  on-primary: '#ffffff'
  primary-container: '#0070eb'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc6ff'
  secondary: '#00677e'
  on-secondary: '#ffffff'
  secondary-container: '#00d2fd'
  on-secondary-container: '#005669'
  tertiary: '#4e5e68'
  on-tertiary: '#ffffff'
  tertiary-container: '#667781'
  on-tertiary-container: '#fbfcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#b4ebff'
  secondary-fixed-dim: '#3cd7ff'
  on-secondary-fixed: '#001f27'
  on-secondary-fixed-variant: '#004e5f'
  tertiary-fixed: '#d3e5f1'
  tertiary-fixed-dim: '#b7c9d5'
  on-tertiary-fixed: '#0c1e26'
  on-tertiary-fixed-variant: '#384953'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
---

## Brand & Style
The design system is engineered to project clinical precision, high-tech reliability, and calm authority. It targets healthcare professionals and researchers who require data-dense information presented with zero visual friction.

The aesthetic is **Medical Minimalism mixed with Glassmorphism**. It utilizes ultra-clean surfaces, expansive white space, and subtle depth to organize complex AI-driven kidney diagnostics. The interface should feel "breathable" and hygienic, mimicking a high-end modern laboratory. 

Visual priorities include:
- **Optical Clarity:** High legibility and distinct information hierarchy.
- **Glassmorphism:** Using depth and transparency to separate diagnostic layers without breaking the flow of the page.
- **Clinical Precision:** Every element is aligned to a strict grid, ensuring a sense of order and medical-grade stability.

## Colors
The palette is rooted in high-luminosity whites to maintain a "clinical" sterile feel, punctuated by high-vibrancy blues that signal intelligence and trust.

- **Primary (Medical Blue):** Reserved for primary actions, critical data highlights, and brand presence.
- **Secondary (Clinical Teal):** Used for interactive sub-elements, success states, and AI-driven insights.
- **Surface:** Surfaces use a semi-transparent white (Alpha 70-80%) to allow the soft blue radial background gradient to subtly bleed through, creating a sense of depth.
- **Semantic Colors:**
    - **Success:** #10B981 (Emerald)
    - **Warning:** #F59E0B (Amber)
    - **Critical/Alert:** #EF4444 (Rose)

## Typography
This design system relies exclusively on **Inter** to ensure maximum legibility across dense medical datasets. 

- **Weight Usage:** Use `600` (Semi-bold) for section headers and `700` (Bold) sparingly for high-level numbers or primary titles. 
- **Scale:** Maintain generous line-heights to prevent ocular fatigue during long diagnostic sessions.
- **Labels:** Small labels (`label-sm`) should use uppercase styling with increased letter spacing to differentiate them from patient data text.

## Layout & Spacing
The layout follows a **Fluid Grid** model with a heavy emphasis on "Safe Zones" to ensure diagnostic charts are never cramped.

- **Grid:** A 12-column grid for desktop with 24px gutters. On mobile, transition to a single-column layout with 16px margins.
- **Rhythm:** Use an 8px base unit. Component padding should lean towards the larger side (e.g., 24px internal padding for cards) to maintain the "Airy" feel of the clinical brand.
- **Alignment:** All data points within lists or tables must be strictly baseline-aligned to ensure the eye can scan across rows without interruption.

## Elevation & Depth
Depth is created through **Glassmorphism** rather than traditional heavy shadows. This keeps the UI feeling lightweight and digital.

- **Surfaces:** Use `backdrop-filter: blur(20px)` on all primary containers.
- **Borders:** Containers must have a 1px solid border using a very low-opacity primary color (`rgba(0, 122, 255, 0.1)`) or pure white (`rgba(255, 255, 255, 0.5)`).
- **Shadows:** Only use shadows for "Floating" elements like tooltips or modals. Use a large blur (32px) with very low opacity (5-8%) and a subtle blue tint to match the Medical Blue theme.
- **Layers:** 
    - Layer 0: Radial Gradient Background.
    - Layer 1: Glass Cards (The workspace).
    - Layer 2: Inset UI elements (Inputs, secondary buttons).

## Shapes
The shape language is **Rounded**, striking a balance between the friendliness of a modern app and the structural integrity of medical software.

- **Standard Elements:** 8px (0.5rem) radius for buttons and input fields.
- **Large Containers:** 16px (1rem) for cards and main diagnostic panels.
- **Progress Bars:** Fully rounded (pill) to represent organic flow and continuity.

## Components
Consistent component styling ensures the application feels like a single, integrated medical tool.

- **Buttons:** 
    - **Primary:** Solid `Medical Blue` with white text. No gradient.
    - **Secondary:** Transparent background with a `Medical Blue` 1.5px border.
- **Input Fields:** Soft gray background (`#F8FAFC`) with an 8px radius. On focus, transition border to `Clinical Teal` with a subtle outer glow.
- **Diagnostic Cards:** White glass (`rgba(255, 255, 255, 0.8)`) with a 1px white border. Use these to wrap all charts and patient summaries.
- **Chips/Badges:** Use "Clinical Teal" at 10% opacity for the background and 100% opacity for the text to indicate categories or status tags.
- **Data Tables:** Remove all vertical lines. Use subtle horizontal dividers in `#F1F5F9`. The header row should be `label-sm` in a muted neutral color.
- **AI Insight Component:** A specialized card variant using a thin `Clinical Teal` border and a very subtle inner glow to denote AI-generated content.