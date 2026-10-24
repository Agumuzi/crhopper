# Website maintenance

CR-Hopper's public website is a static, dependency-free project page under the /docs folder.

## Enable publication

Open Settings > Pages in the crhopper repository.
Under Build and deployment, select Deploy from a branch.
Choose the main branch and the /docs folder, then Save.

Once deployed, the public URL is https://agumuzi.github.io/crhopper/.

## Source files

- index.html: semantics, content, navigation and meta tags.
- assets/style.css: responsive dark terminal and pixel styling.
- assets/app.js: English, Chinese, Russian, Persian translations and copy-link interactions.
- assets/rocket.svg: compact, resolution-independent pixel-rocket identity.
- .nojekyll: direct static publishing.

## Constraints

The operational subscription files MUST remain at the repository root with their exact names:
CR-Hopper.txt and CR-Hopper.yaml.

Do not change their raw URLs for website or branding updates. The website is a presentation layer only; it does not operate or validate proxy nodes.

Keep any live node counts, real-time health, uptime or privacy claims off the site unless backed by trustworthy runtime data.

If a separate feed publisher rebuilds or force-pushes the repository, ensure it preserves the docs folder and README translations.

GitHub About, Topics, and Social preview are managed in the repository's own Settings and are not automatically configured by this static website.
