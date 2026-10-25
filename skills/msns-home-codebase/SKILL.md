---
name: msns-home-codebase
description: >
  Comprehensive codebase memory for the msns-home public website project. Use this skill to recall the architecture, routing, SEO, API endpoints, S3 integrations, and tech stack without having to scan the repository.
---

# MSNS Home (Public Website) Codebase Memory

## Overview
- **Name:** MSNS Public Website
- **Domain:** `msns.edu.pk`
- **Purpose:** Public-facing marketing website for M.S. Naz High School.
- **Stack:** T3 Stack (Next.js 15 App Router, React 18, TypeScript 5.9.3, Node.js).
- **Package Manager:** npm 10.8.3, ESM (`"type": "module"`).

## Technology Stack
- **Framework:** Next.js 15.5.9 (App Router).
- **Language:** TypeScript 5.9.3 (strict mode).
- **Styling:** Tailwind CSS v4.1.16 + shadcn/ui (new-york style, neutral base color).
- **Animations:** Framer Motion 12.4.7.
- **3D Graphics:** Three.js 0.170, @react-three/drei, @react-three/fiber (for InfiniteGallery).
- **Data Fetching:** tRPC 11.8.1, TanStack React Query 5.50.
- **Storage:** AWS S3 (via Cloudflare R2).
- **Auth:** scaffolded (next-auth 5.0.0-beta.30) but UNUSED.
- **Deployment:** Vercel.

## Routing Structure (App Router)
- **`/` (Home):** Hero, Features, InfiniteGallery (3D), QuickLinks, Testimonials, CTA, PopupAd.
- **`/about`:** HeroSection, MessageFromCEO, MissionStatement, KeyStatistics, SchoolValues (parallax/Framer Motion heavy).
- **`/admission`:** Admission info, fee structure, criteria, FAQ.
- **`/contact`:** Contact info with GeometricBackground.
- **`/terms-of-service`:** Terms of service.
- **Pattern:** `page.tsx` (Server Component for SEO metadata) → `*-client.tsx` (Client Component for interactivity).

## API Routes (`/api/`)
- `/images/[...key]`: S3 image proxy (streams images from Tigris S3, immutable cache 1yr).
- `/images/resolve/[filename]`: Filename resolver (finds image by basename across folders).
- `/gallery`: Lists gallery images from S3 (gallery/ + videos/ prefixes).
- `/gallery/[...key]` (DELETE): Deletes image from S3 (Requires `GALLERY_API_SECRET`).
- `/gallery/upload` (POST): Uploads image to S3 (Requires `GALLERY_API_SECRET`).
- `/google-reviews`: Fetches Google Place reviews via Maps API.
- `/trpc/[trpc]`: Standard tRPC handler (currently only has placeholder `post.hello` procedure).

## Component Organization
- **UI:** `src/components/ui/` (52 shadcn/ui components).
- **Blocks:** `src/components/blocks/`
  - `landing/`: 22 page-level section components (HeroSection, FeaturesSection, InfiniteGallery, popup-ad, etc.)
  - `nav/`: Header.tsx (fixed, scroll effects, framer motion).
  - `nav/footer/`: Large footer with newsletter, social, affiliations, etc.

## SEO Implementation
- **Metadata:** Per-page `Metadata` exports (title, description, canonical, OpenGraph).
- **Structured Data:** `SEOSchema.tsx` (JSON-LD SchoolSchema, BreadcrumbSchema, AggregateOfferSchema).
- **Sitemap/Robots:** Dynamic `sitemap.ts` for all pages; detailed `robots.txt` blocking AI crawlers.
- **Google Integration:** Verification meta tag, AdSense (`ca-pub-1351871288722699`), Tag Manager, Microsoft Clarity.
- **PWA:** `manifest.json` with app icons and shortcuts.

## File & Asset Handling (Connection to msns-build)
- **Shared Storage:** Uses the same Tigris S3 bucket as `msns-build`.
- **Image Serving:** ALL images are served through Next.js API as a proxy to S3 (`/api/images/...`). No external image domains configured.
- **LMS Connection:** No code-level connection to `msns-build`. Linked via URLs (`https://lms.msns.edu.pk`).
- **Migration Scripts:** `migrate_final.js` and `migrate_images.js` used to migrate from Cloudinary to Tigris S3.

## Environment Variables
- **Active:** Tigris S3 credentials (`AWS_ENDPOINT_URL`, `AWS_DEFAULT_REGION`, `AWS_S3_BUCKET_NAME`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`).
- **Unused/Legacy:** `DATABASE_URL` (no database is actually used), `AUTH_*` (no auth implemented).

## Styling Approach
- Tailwind v4 with CSS-in-JS theme variables (oklch color system).
- CSS custom properties for light/dark mode (`:root` and `.dark`).
- Custom utilities (`scrollbar-hide`, container with 1400px max-width) and animations (`marquee-left`, `marquee-right`).

## Known Issues / Quirks
- Broken link in `Header.tsx`: `href="/https://lms.msns.edu.pk"` (leading slash makes it relative).
- T3 Scaffold remnants: Prisma/DB and next-auth are scaffolded but entirely unused.
- Legacy URLs: `manifest.json` still has some Cloudinary URLs.
