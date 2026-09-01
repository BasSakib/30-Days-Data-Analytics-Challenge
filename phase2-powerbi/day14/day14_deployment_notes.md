# Day 14 — Final Deployment: Publish & Share — Solution Notes

## Pre-publish checklist
- Every page reviewed: no leftover test visuals, no placeholder text
- Titles present and clear on every visual
- Slicers reset to a sensible default state (or explicitly set "Full View"
  bookmark as the page's default)
- File saved as `day14_solved.pbix` (final polished version)

## Publish workflow (requires a Power BI account / Pro or PPU license)
1. **Home → Publish** → sign in → select a destination **workspace**
   (e.g. "My Workspace" for personal use, or a named team workspace)
2. Power BI uploads the `.pbix` and creates a matching **Dataset** +
   **Report** in the Power BI Service (app.powerbi.com)

## Scheduled refresh
- Because this report's source is a local file (CSV), a **scheduled
  refresh** requires an **On-premises Data Gateway** installed on a
  machine that can reach that file path — the Service can't refresh
  from a laptop's local disk on its own.
- If the source were a cloud source instead (SharePoint, a database, a
  web API), no gateway would be needed — the Service can refresh those
  directly, e.g. Dataset settings → Scheduled refresh → set frequency.
- For a portfolio project, this limitation is fine to state as-is; in a
  real company deployment, the fix is either a gateway or moving the
  source to a cloud location.

## Row-level security (RLS)
Only relevant if the report exposes sensitive/segmented data (e.g. each
regional manager should only see their own region):
1. Modeling tab → Manage Roles → New Role, e.g. "RegionManager"
2. Add a DAX filter on `Dim_Region`: `[Region] = USERPRINCIPALNAME()` style
   logic mapped via a role-mapping table, or a simpler static filter per
   role for a small team
3. After publishing, in the Service: Dataset → Security → assign specific
   user emails to each role

## Share vs. App
- **Share via link**: fastest, works for a handful of named individuals,
  each recipient needs at least a Power BI Pro license (or the report
  needs to be in Premium capacity) to view it
- **Share via App**: better for broader distribution to a whole team/org
  — package one or more reports into an App, publish it, and users
  install/open the App instead of individual report links; easier to
  manage permissions and navigation for a larger audience

## Static export
File → Export → **Export to PDF** — produces `day14_solved.pdf`, a
non-interactive but universally shareable snapshot of the final report.
This is the artifact to attach to a portfolio site or email when the
recipient doesn't have Power BI access at all.
