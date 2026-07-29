DocSiteInfo = provider(
    fields = {
        "content_dir": "Directory containing site content",
        "static_dir": "Directory containing site static data",
        "config": "config.yaml for site",
    },
)
DocSectionInfo = provider(
    fields = {
        "output_dir": "Directory containing built section",
    },
)

DocMenuItem = provider(
    fields = {
        "name": "Name displayed in menu",
        "url": "URL menu item links to",
        "pageRef": "Relative page reference item links to",
        "weight": "Weight of menu item",
        "data": "Files to include when building DocMenuItem",
    }
)
