# mpv-bookmark-player

Search through browser bookmarks and play them with mpv. Currently only supports Firefox.

## Requirements

Python, [mpv](https://github.com/mpv-player/mpv) and [fzf](https://github.com/junegunn/fzf) should be installed and in your PATH.

## Usage

1. Clone this repository.
2. Change the `FIREFOX_PROFILE_DIR` variable in `config.py` to your Firefox profile directory. You can find this by going to `about:support` in Firefox.
3. Make `bookmark-player` executable by running `chmod u+x bookmark-player`.
4. Run `./bookmark-player`.

## Running `bookmark-player` Anywhere

Create a symbolic link to `bookmark-player` in a directory that is in your PATH.
