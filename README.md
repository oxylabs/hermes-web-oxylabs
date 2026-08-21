[![Oxylabs promo code](https://github.com/oxylabs/hermes-web-oxylabs/blob/main/Github%20repositories%20banner%20v1%402x.png)](https://oxylabs.io/hermes-web-oxylabs?&utm_content=web_api_waitinglist&groupid=877)

# Hermes Web Oxylabs

Give [Hermes Agent](https://github.com/NousResearch/hermes-agent) web search
and webpage extraction powered by Oxylabs AI Studio.

Use this plugin when an agent needs current web context, clean page content, or
research-ready source material from public webpages. It helps Hermes work with
structured, LLM-ready web data instead of raw page noise.

## What it does

- **Web search:** returns ranked results with titles, URLs, and descriptions.
- **Web extraction:** turns webpages into readable markdown.
- **Agent-friendly output:** gives Hermes cleaner material for summaries,
  comparisons, notes, and follow-up reasoning.

The standard Hermes `web_extract` tool currently requests markdown with
JavaScript rendering disabled and does not expose geo-location controls to the
agent. The Oxylabs provider accepts output-format, JavaScript-rendering, and
geo-location options for forward compatibility, but Hermes core does not
currently make those options model-callable.

## Good for

- Research agents that need fresh web context.
- Product, market, and competitive research across public sources.
- Turning webpages into clean summaries, tables, briefs, or notes.
- Turning noisy public pages into cleaner source material.

## Install

```bash
hermes plugins install oxylabs/hermes-web-oxylabs --enable
```

Set your Oxylabs AI Studio API key:

```bash
export OXYLABS_API_KEY="..."
```

You can also put the key in `~/.hermes/.env`:

```bash
OXYLABS_API_KEY=...
```

Then select Oxylabs:

```bash
hermes config set web.search_backend oxylabs
hermes config set web.extract_backend oxylabs
```

Or configure both with the shared backend:

```yaml
web:
  backend: "oxylabs"
```

After changing plugin, backend, or API key settings, start a new Hermes session
or restart the Hermes gateway.

## Links

- Oxylabs AI Studio: https://aistudio.oxylabs.io
- AI Studio apps: https://aistudio.oxylabs.io/apps/
- API key page: https://aistudio.oxylabs.io/api-key
