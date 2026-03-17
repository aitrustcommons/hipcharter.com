"""
Slice the v8 HIP Charter poster into section images for website use.
Renders the full HTML, then captures specific zones as separate PNGs.
"""
import asyncio
from playwright.async_api import async_playwright

OUTPUT_DIR = "/home/claude/hipcharter.com/docs/assets/images"
HTML_PATH = "/home/claude/hipcharter.com/visual-concepts/v8-split-color-poster.html"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1400, "height": 3000})
        await page.goto(f"file://{HTML_PATH}")
        await page.wait_for_timeout(1000)

        # 1. Four singles row (the four patterns)
        singles = page.locator(".singles-row")
        await singles.screenshot(path=f"{OUTPUT_DIR}/hip-charter-four-patterns-foundation-tooling-pipeline-integration.png")
        print("1. Four patterns captured")

        # 2. Six pairs row (pairwise overlaps)
        pairs = page.locator(".pairs-row")
        await pairs.screenshot(path=f"{OUTPUT_DIR}/hip-charter-six-pairwise-overlaps.png")
        print("2. Six pairwise overlaps captured")

        # 3. Triples + Center (convergence)
        # Capture triples row and center card together
        triples = page.locator(".triples-row")
        center = page.locator(".center-card")
        triples_box = await triples.bounding_box()
        center_box = await center.bounding_box()
        if triples_box and center_box:
            clip = {
                "x": min(triples_box["x"], center_box["x"]),
                "y": triples_box["y"],
                "width": max(triples_box["width"], center_box["width"]),
                "height": (center_box["y"] + center_box["height"]) - triples_box["y"]
            }
            await page.screenshot(path=f"{OUTPUT_DIR}/hip-charter-convergence-triples-center.png", clip=clip)
            print("3. Convergence (triples + center) captured")

        # 4. Gap zone (Intent Layer + Unknown)
        gap = page.locator(".zone-gap")
        await gap.screenshot(path=f"{OUTPUT_DIR}/hip-charter-intent-layer-gap.png")
        print("4. Intent Layer gap captured")

        # 5. Human Intelligence zone
        human_zone = page.locator(".zone-human")
        await human_zone.screenshot(path=f"{OUTPUT_DIR}/hip-charter-human-intelligence-zone.png")
        print("5. Human Intelligence zone captured")

        # 6. AI Intelligence zone
        ai_zone = page.locator(".zone-ai")
        await ai_zone.screenshot(path=f"{OUTPUT_DIR}/hip-charter-ai-intelligence-zone.png")
        print("6. AI Intelligence zone captured")

        # 7. Full partnership zone (the entire middle section)
        partner_zone = page.locator(".zone-partner")
        await partner_zone.screenshot(path=f"{OUTPUT_DIR}/hip-charter-partnership-zone-full.png")
        print("7. Full partnership zone captured")

        await browser.close()
        print(f"\nAll images saved to {OUTPUT_DIR}")

asyncio.run(main())
