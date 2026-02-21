# Casa Gianelli - Project Handoff

## Project Overview

Casa Gianelli is the Gianelli family's personal command center. A full-featured Streamlit dashboard with 19 pages covering family logistics, health tracking, entertainment, voice tools, and Gian Lucca's developmental world. Built for Peter and Gladys. Currently at v3.0 (Sidebar Navigation Edition).

**Tagline:** La Familia. Peter & Gladys & Gian Lucca.

## Architecture

- **Framework:** Streamlit (v1.41+)
- **AI Backend:** Azure OpenAI (chat completions via shared client)
- **Structure:** Modular. Main app.py routes to individual tab modules.
- **State:** Centralized session_state initialization in utils/state.py
- **AI Client:** Shared wrapper in utils/ai_client.py

## Key Files

| File | Purpose |
|------|---------|
| `app.py` | Main app. Page registry, sidebar nav, CSS, routing (317 lines) |
| `utils/state.py` | Central session_state defaults (grocery, tasks, health, GL tracking, chat histories) |
| `utils/ai_client.py` | Shared Azure OpenAI client + reusable chat/render_chat functions |
| `utils/sign_data.py` | Baby sign language reference data |
| `requirements.txt` | streamlit, pandas, plotly, openai |
| `.streamlit/secrets.toml` | Azure OpenAI credentials (gitignored) |

## Page Registry (19 Pages, 5 Groups)

### Family HQ
| Page | Module | Purpose |
|------|--------|---------|
| Casa | `tab_casa.py` | Shopping search (Amazon, Costco, Target, Walmart, Instacart) + food ordering (DoorDash, Uber Eats) + favorites |
| Housing Search | `tab_housing.py` | Palm Springs & Big Bear rental search. Links to all platforms. Saves picks with details. |
| Car Search | `tab_car.py` | Car search functionality |
| Grocery List | `tab_grocery.py` | Categorized grocery list (electrolytes, broth, protein, staples, Costco, baby) |
| Calendar | `tab_calendar.py` | Family events and reminders |
| Tasks | `tab_tasks.py` | Task list with assignees (Peter/Gladys) and done states |

### Health & Wellness
| Page | Module | Purpose |
|------|--------|---------|
| Health Protocol | `tab_health.py` | 6-week peptide/TRT protocol tracker. Injection log with site rotation. Weekly check-ins (weight, energy, sleep, mood, libido). Weight chart via Plotly. Separate protocols for Peter and Gladys. |
| Gladys Beauty | `tab_beauty.py` | Beauty scheduling and tracking |

### Entertainment
| Page | Module | Purpose |
|------|--------|---------|
| Music Discovery | `tab_music.py` | Music discovery tool |
| Streaming | `tab_streaming.py` | Streaming recommendations and watchlist |

### Voice
| Page | Module | Purpose |
|------|--------|---------|
| Peter Vomit | `tab_peter_vomit.py` | Brain dump tool. No filter, no structure. Drop tagged thoughts (Work, Personal, Idea, Family, Music, Health, Money, Random). Recent drops with color-coded tags. |
| Gladys Bamba | `tab_gladys_bamba.py` | Gladys's version of the brain dump |

### GL's World (7 pages for Gian Lucca's development)
| Page | Module | Prompt File | Purpose |
|------|--------|-------------|---------|
| Story Buddy | `tab_story_buddy.py` | `prompts/story_buddy.py` | Interactive storytelling for Liam & Logan (Wilson boys) |
| GL Stories | `tab_gl_stories.py` | `prompts/gl_story_buddy.py` | Story Buddy tailored for Gian Lucca |
| GL Languages | `tab_gl_languages.py` | `prompts/gl_languages.py` | Trilingual vocab cards (English/Italian/Spanish) with pronunciation guides. 6 themes: Family, Food, Animals, Colors, Body, Nature. Chat with Language Buddy. |
| GL Signs | `tab_gl_signs.py` | `prompts/gl_signs.py` | Baby sign language coach. Priority signs (MORE, ALL DONE, MILK, etc.) |
| GL Games | `tab_gl_games.py` | `prompts/gl_games.py` | Age-matched cognitive development activities |
| GL Milestones | `tab_gl_milestones.py` | `prompts/gl_milestones.py` | Developmental milestone tracker (CDC-based) |
| GL Music | `tab_gl_music.py` | `prompts/gl_music.py` | Music-based brain development. Leverages Peter's DJ background. |

## GL Age Tracking

- **Born:** July 27, 2025
- **Tracked via:** `utils/state.py` `gl_age()` function
- **Displays:** months, weeks, days, and "Day X of 1,000" (first 1,000 days concept, counting from conception)
- **Shown in sidebar** on every page

## State Management

All session state initialized centrally in `utils/state.py`. Key state groups:
- **grocery_items / grocery_checked:** Pre-populated categories with health-focused defaults
- **tasks:** Pre-loaded task list with assignees
- **injection_log / checkin_log:** Health protocol tracking
- **peter_drops / gladys_drops:** Brain dump entries
- **housing_picks / car_picks:** Saved search results
- **gl_signs_learned / gl_milestones_done / gl_vocab_practiced / gl_games_done / gl_music_reactions:** GL development tracking
- **Chat histories:** Separate message arrays for each AI-powered page (sb_messages, gl_sb_messages, gl_lang_messages, gl_signs_messages, gl_games_messages, gl_miles_messages, gl_music_messages)

## Design

- **Color scheme:** Dark warm theme. Black/brown sidebar (#1A0F0F), crimson red (#C41E3A), gold (#D4A017)
- **Fonts:** Playfair Display (headings), Lato (body)
- **Sidebar:** Dark gradient with gold accents, GL age display, live task/sign/milestone counts

## Current Status

- All 19 pages functional
- AI chat integrated on 7+ pages
- Health protocol tracker with injection logging and weight charting
- Housing search with multi-platform links for Palm Springs and Big Bear
- GL developmental tools fully operational with age-specific prompts
- No persistent storage (all state resets on restart)
- No authentication

## Open Items

1. No persistent storage. Everything is session_state only. Database or file persistence needed for injection logs, check-ins, task completions, GL milestones.
2. No Dockerfile. No deployment config. Running locally only.
3. Car Search and Streaming tabs may be minimal/placeholder.
4. No authentication layer.
5. Watchlist state exists but unclear if the streaming tab uses it.
6. Calendar events hardcoded to a single default entry.

## Dependencies

```
streamlit>=1.41.0
pandas
plotly
openai
```

## How to Run

```bash
cd C:\Claude\Work\casa-gianelli
pip install -r requirements.txt
streamlit run app.py
```
