# TV Setup (googletv / android tv)
One of the best TV OS is Google TV. Here are some reasons why you should consider using Google TV:
- Sideloading apps is straightforward on Google TV. You can install apps like Stremio, SmartTube, and others.
- It's not as responsive as Apple TV, but you can tweak it to make it faster.
- You can use alternative launchers like 'Projectivy'.

**Table of contents**
<!-- TOC -->
* [TV Setup (googletv / android tv)](#tv-setup-googletv--android-tv)
  * [All TV types:](#all-tv-types)
  * [Google TV OS:](#google-tv-os)
    * [Best google TV apps:](#best-google-tv-apps)
<!-- TOC -->

## All TV types:
- My first advice is to never use the standard mode on your TV. Always use the cinema/ filmaker or movie mode. The
  standard mode is too bright and the colors are not accurate. Use the cinema or movie mode when watching movies or
  series.
- Here is a [video](https://www.youtube.com/watch?v=dY3M_h30HYc) explaining TV modes.
  And [this video](https://www.youtube.com/watch?v=nTO2Wmw1NKA) for changing the settings of your TV taking into
  account different modes (SDR, HDR, Dolby). (You can refer to reddit guides or YouTube videos
  or [rtings.com](https://rtings.com) to find the best settings).
- If your TV supports multiple content types (SDR, HDR, DOLBY), the mode needs to be activated on each content type.
- On some TVs like the Hisense U7k, you need to enable enhanced HDMI mode to access dolby vision & 60HZ on your
  Chromecast and other HDMI inputs.
- If you play video games, use the game mode. It will reduce the input lag and improve the gaming experience.

## Google TV OS:
- (Important) Enhance the performance of your Google TV by following
  this [tutorial](https://www.slashgear.com/1321192/tricks-make-chromecast-google-tv-run-faster/)
- Chromecast google TV
  4k [video settings](https://www.reddit.com/r/Chromecast/comments/1ct77ai/a_fix_for_washed_out_colors_and_performance/)
- Chromecast google TV remote: you can use your iPhone or android to remotely control google tv and use your
  phone's keyboard, for example. You need either Google TV app or Goohle home app on you phone. on your google
  TV, the feature is disabled by default: you need to go to system-> keyboard -> manage keyboards -> check
  virtual remote. You can now use your phone to type things rapidely
- Windows 11 with 4K HDR TV: follow this [tutorial 1](https://www.pcmag.com/how-to/set-up-gaming-pc-on-4k-tv)
  and [tutorial 2](https://www.pcmag.com/how-to/how-to-play-games-watch-videos-in-hdr-on-windows-10)
- recommended TV apps for Google TV: Projectivy launcher, stremio, Smart Tube, YouTube atv. update the channels in
the Projectivy and add stremio there. Also make it the default launcher for your tv.

### Best google TV apps:
- [SmartTube](https://smartyoutubetv.github.io/): A free Android TV app alternative to youtube with no ads, designed for TV screens, up to 8K video resolution, supports youtube accounts.
- [Projectivy Launcher](https://play.google.com/store/apps/details?id=com.spocky.projengmenu&hl=en&pli=1):  an alternative app launcher for Android TV devices that provides users with a different home screen and method for navigation and opening apps.
  -  Remember to export your settings: https://www.reddit.com/r/Projectivy_Launcher/comments/1cdt00f/tell_me_about_exporting_these_launcher_settings/
  -  You can create channels in the menu and add stremio, smartube, spotify to the home screen.
- [Stremio](https://www.stremio.com/)
   #### What is Stremio ?
  <img width="1908" height="912" alt="image" src="https://github.com/user-attachments/assets/1f5388f6-3a97-4d7a-b5e1-d66eaea07728" />

  - Stremio is a video streaming application that allows you to watch and organize video content from different services,
    including movies, series, live TV and video channels. The content is aggregated by an addon system providing streams
    from various sources. And with its commitment to security, Stremio is the ultimate choice for a worry-free,
    high-quality streaming experience.
  - You can either use your favorite platforms to watch movies or series or use torrent without any risk.
  - Stremio is available on all platforms: Web, Windows, Mac, Linux, Android, iOS, Android TV, Apple TV...
  - Addons...etc will be synchronized between all your devices.
  - [A fast tutorial to get it work](https://arnav.au/2025/04/16/stremio-torrentio-debrid-how-to-guide/)
  - [A complete and detailed tutorial](https://guides.viren070.me/stremio/)
  - You will use a debrid service (like Real Debrid, All Debrid), so you won't need any VPN.
    What is a debrid service? A debrid service is an unrestricted multi-hoster that allows you to stream and download videos instantly at the best speeds. In plain English, the debrid services act as a proxy between the BitTorrent tracker and you, so you download the content directly from their servers at high speed. Most of the content is already cached, meaning you can instantly access it. Personnaly, I use ALL Debrid, but others exist like : TorBox, Real Debrid...

  #### Installation
  - (Update November 2025)
  - Setup :
      - After making any change to any addon, you don't need to close the application to synchronize the changes, just click on the addons tab, and go back to home.
        - My recommended Setup:
          - AIOStreams:

              #### 🌐 AIOStreams + Stremio Configuration Guide

              ##### 🧩 What is AIOStreams?
              AIOStreams is an all-in-one **Stremio addon manager** that lets you organize, install, and sync all your favorite addons in one place.
              It also allows you to **save your configuration online**, so you don’t lose your setup.

              Your data is linked to a **UUID** (your unique ID) and a **password**, so you can restore your configuration anytime.

              ---

              ##### 🪪 Step 1 — Login to Stremio Web
              Go to 👉 [https://web.stremio.com/](https://web.stremio.com/)
              Log in with your regular Stremio account.

              ---

              ##### ⚙️ Step 2 — Open AIOStreams
              Visit 👉  [https://aiostreamsfortheweebs.midnightignite.me/](https://aiostreamsfortheweebs.midnightignite.me/)
              Your can also use the [AIOStreams (ElfHosted)](https://aiostreams.elfhosted.com/) but it is limited to 10 addons and there is no Torrentio support.

              This page is where you manage everything related to your addons.

              ---

              ##### 🧱 Step 3 — Create Your Configuration
              1. Go to the **“Save and Install”** section.
              2. Enter a **password** of your choice — this will create your AIOStreams account.
              3. You’ll receive a **UUID** (like your username).
              4. **Save both the UUID and your password!** You’ll need them to restore or import your configuration later.

              ---

              ##### 📂 Step 4 — Import Your Settings
              1. Download[ my configuration file](../src/awesome_os/config/others/aiostreams-config.json)
              2. Go to **“Navigate and Install”**.
              3. Click **Import**.
              4. Select and upload your saved configuration file. You will an error message saying that 'StreamFusion API Key is invalid' which is normal for now.

              Your addons and settings will load automatically.

              ---

              ##### 🔑 Step 5 — Enable Your Debrid Services and TMDB API
              1. In AIOStreams, go to **Services**.
              2. Enable your preferred **Debrid service** (e.g.,  AllDebrid, Real-Debrid, TorBox).  I am using All Debrid, if you choose another Debrid provider, you will need to edit the provider in each addon (which is very easy since it's just a select box)
              3. Enter your API key.
              4. After adding your Debrid api key, go down and look for 'TMDB' and follow the instructions to add your TMDB API keys.

              ---

              ##### (Optional) Step 6 — Configure Ratings, Debdrid Statuts, French Addons and AI Search
              Go to the **Addons** section. You’ll see a list of installed addons.
              Some may be deactivated (unsupported ones for now by AIOStreams).

              ###### ⚙️ (optional) Configure *Ratings (custom)*:
              1. Configure your rating addon https://72059fbbd1e5-stremio-addon-ratings.baby-beamup.club
              2. Go back to AIOStreams, and copy the manifest URL in the 'Ratings (custom)' manifest URL field.
              3. Save and enable the addon.

              ###### ⚙️ (optional) Configure *Statusio (custom)*:
              1. Configure your statusio addon https://statusio.elfhosted.com/configure
              2. Go back to AIOStreams, and copy the manifest URL in the 'Statusio (custom)' manifest URL field.
              3. Save and enable the addon.

              ###### ⚙️ (optional) Configure *Top-Streaming (custom)*:
              1. Configure your statusio addon https://top-streaming.stream/configure?lang=en
              2. In Poster type, select 'Standard Posters'
              3. Go back to AIOStreams, and copy the manifest URL in the 'Top-Streaming (custom)' manifest URL field.
              4. Save and enable the addon.

              ###### ⚙️ (🇫🇷  optional) Configure French addon *CometFR (custom)*:
              1. Configure your CometFR addon https://comet.stremiofr.com/
              2. Go back to AIOStreams, and copy the manifest URL in the 'CometFR (custom)' manifest URL field.
              3. Click **Copy Link** — the link should start with
                 `https://comet.stremiofr.com/`
                 and end with `=/manifest.json`.
              4. Go back to AIOStreams, paste this link in the URL field, click on 'update' at the bottom of the configuration and **Activate** the addon with the switch button.

              ###### ⚙️ (🇫🇷  optional) Configure French addon *JackettioFR (custom)*:
              1. Configure your JackettioFR addon https://jackettio.stremiofr.com/
              2. Go back to AIOStreams, and copy the manifest URL in the 'JackettioFR (custom)' manifest URL field.
              3. A **Stremio Link** will appear — right-click and choose **Copy link**.
                 It should start with
                 `https://jackettio.stremiofr.com/`
                 and end with `=/manifest.json`.

             ###### ⚙️ (🇫🇷  optional) Configure French addon *StremFusion*:
              1. Click the **Edit** button.
              2. look for StreamFusion API Key and follow the instructions toget the api key from the telegram bot.
              3. Copy the key, click on 'update' at the bottom of the configuration and **Activate** the addon with the switch button.

              ###### ⚙️ (optional) Configure *AI Search (custom)*:
             1. Configure your AI Search addon https://stremio.itcon.au/
              - It is preferable to use this addon with Trakt.
              - Follow the tutorial on their website to get the api keys.
             1. Go back to AIOStreams, and copy the manifest URL in the 'JackettioFR (custom)' manifest URL field.

              ###### ⚙️ (optional) reorder the addons and remove Cinemeta catalogs:
              This will remove the 4 first default catalogs provided by Stremio using their official addon named 'Cinemeta'. We can remove this and controle everything needed using TMDB Addon.
              1. Go to [cinebye website](https://cinebye.dinsden.top/)
              2. Go to section #1 Called 'Authenticate' and login using your stremio credentials (or use the auth key with this command in the console in web.stremio.com `JSON.parse(localStorage.getItem("profile")).auth.key` )
              3. Go to section #2 called 'Options' and uncheck these functionalities :
                 - (Optional) Remove Cinemeta Search. (Will be replaced by AIOMetadata search)

                 - (Recommended) Remove Cinemeta Catalogs. Will be replaced by TMDB catalogs with the ratingd.

                 - (Warning) Remove Cinemeta Metadata. This will break your Trakt Sync and Calendar functionalities. Do not uncheck it unless you want this.
              4. Go down until you see the list of installed addons, reorder the addons, put cinemeta last.
              5. Go to section #3 Called 'Sync Addons' and click on 'Sync to Stremio'.

              ---

              ##### 💾 Step 7 — Save and Install
              1. Go back to the **Install** section.
              2. Click **Save** — this saves your configuration to your online AIOStreams account.  If you see a timeout error with the name of an addon, it means that this addon is down right now. Just deactivate it and save again (sometimes StremFusion and Opensubtitles V3+ are down)
              3. Then click **Install** and choose **Stremio Web** (or your preferred option).
              4. Stremio will open and prompt you to install your configured addons.

              ---

              ##### ✅ Step 8 — Test Everything
              Open any movie or TV show in Stremio.
              You should now see your addons providing streams.
              After selecting a movie, you should see this (Ratings and Statutios appears only if you installed them:

              <img width="389" height="719" alt="image" src="https://github.com/user-attachments/assets/fdb37b6a-68f9-4a33-abc6-c1adfd21a699" />

              ---
              As you can see, the streams display clean, readable, and emoji-enhanced stream information inside Stremio. But what does these emojis mean ?

             - 🎞️ Resolution Badges (From top to worse): ⚜️ 4K for 2160p, 📀 1440p, 📀 1080p ...etc ⚪ N/A if resolution is missing

             - 🏷️ Quality Labels (From top to worse): 📀 REMUX, 💿 Blu-ray, 🌐 WEB-DL, 🖥️ WEBRip, 💾 HDRip / DVDRip / HDTV / TS / TC, ⚪ N/A if no quality tag exists

             - Cached streams: [AD⚡️]: The lightning symbol means the stream is cached, ⏳️ means not cached. It's preferable to select a cached stream because a non-cached stream means that you the debrid service will try to download it, and if there isn't any seeders, you won't be able to stream it.

            ##### ✅ Step 9 — Watch an episode of a popular show:
            - If every stream appears with the ⏳ (not cached) icon and none show the ⚡️ (cached) indicator, it usually means your IP address has not been validated on your AllDebrid account.
              Some debrid services (including AllDebrid) require you to confirm your current IP before they allow cached torrents to be accessed.
              So when you start a stream for the first time from a new addon, the service blocks cached access until the IP is verified.

              To fix this:

              Start any stream in Stremio (this triggers the request on the debrid side).

              Go to your debrid service’s website (e.g., AllDebrid).

              You should see a prompt asking you to validate or authorize your IP address.

              Confirm it — and cached streams will immediately switch from ⏳ to ⚡️.
            - Keep your **UUID** and **password** safe — that’s your AIOStreams login.
            - You can restore your setup anytime by re-entering your credentials.
            - AIOStreams makes it easy to sync and manage all your addons from one place.
            - The order of a list (catalogs) in Stremio home is determined by the installation order (except in AIOSteams were you can order them manually).

           Your Stremio should look like this: <img width="1908" height="912" alt="image" src="https://github.com/user-attachments/assets/1f5388f6-3a97-4d7a-b5e1-d66eaea07728" />

     ##### 💡 Stremio Tips
       -  In Stremio Settings, you can select the prefered 'Audio language' and 'Subtitles'. This will automatically set the audio and subs automatically when you watch something. This is not synced between devices, you need to do it manually on each of your device.
       -  Use Stremio web to configure addons. ALl settings & addons will sync between your devices if you use the same
            account.
       - (Optional) Trakt :
          - Trakt is a media tracking service that helps users sync their TV shows and movies across numerous platforms and devices.
          - You can enable trakt in Stremio settings. You can download Trakt mobile app or use their website.
          - Ratings & history: I rank my movies (and series) on trakt (they will automatically mark as watched if you
           activate that setting in trakt's website : settings -> Mark Watched After Rating: Automatically mark unwatched
           items with today's date).
          - If you didn't rate some movies & tv shows, you can add them to history in Trakt to avoid being recommended by the 'AI Search' addon.
         - If you want to syncronize Trakt with IMDB you can use [IMDB-Trakt-Syncer](https://github.com/RileyXX/IMDB-Trakt-Syncer). You can rate what you watch on IMDB or trakt and run the python app to sync everything.
