"""Use playwright to build a gallery of website using this theme."""

from pathlib import Path
from shutil import copy

from playwright.sync_api import TimeoutError, sync_playwright
from rich import print
from rich.progress import track
from yaml import safe_load


def regenerate_gallery() -> None:
    """Regenerate images of snapshots for our gallery.

    This function should only be triggered in RTD builds as it increases the build
    time by 30-60s. Developers can still execute this function from time to time to
    populate their local gallery images with updated files.
    """
    # get the existing folders path
    _static_dir = Path(__file__).parents[1] / "_static"

    # create the static gallery folder where we'll put the gallery source files
    gallery_dir = _static_dir / "gallery"
    gallery_dir.mkdir(exist_ok=True)

    # load gallery data
    gallery_items = safe_load((_static_dir / "gallery.yaml").read_text())
    image_404 = _static_dir / "404.png"

    with sync_playwright() as p:
        # Generate our browser to visit pages and generate images
        for ii in range(3):
            try:
                browser = p.chromium.launch()
                break
            except TimeoutError:
                print(f"Browser start timed out. Trying again (attempt {ii+2}/3)")
        page = browser.new_page()

        for item in track(gallery_items, description="Generating screenshots..."):
            item["id"] = item["title"].lower().replace(" ", "_")
            screenshot = gallery_dir / f"{item['id']}.png"

            # Visit the page and take a screenshot
            for ii in range(3):
                try:
                    page.goto(item["link"])
                    page.screenshot(path=screenshot)
                    break
                except TimeoutError:
                    print(f"Page visit start timed out for: {item['link']}")
                    print(f"Trying again (attempt {ii+2}/3)")

            # copy the 404 only if the screenshot file was not manually
            # generated by a maintainer
            if not screenshot.is_file():
                print(f"Could not generate screenshot for {item['title']}, using 404.")
                copy(image_404, screenshot)

        # Clean up the browser since we no longer need it
        browser.close()
    print(f"Finished generating gallery images at: {gallery_dir}")


if __name__ == "__main__":
    regenerate_gallery()