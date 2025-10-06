# Use Debian Bookworm Slim for minimal image size
FROM debian:bookworm-slim

# Install Pandoc, LaTeX (full), and comprehensive font support for ALL languages
RUN apt-get update -y && apt-get install -y \
    pandoc \
    texlive-full \
    curl \
    fontconfig \
    # Install ALL Noto fonts for comprehensive Unicode coverage
    # This covers 1000+ languages and all major scripts
    fonts-noto \
    fonts-noto-cjk \
    fonts-noto-cjk-extra \
    fonts-noto-color-emoji \
    fonts-noto-extra \
    fonts-noto-ui-core \
    fonts-noto-ui-extra \
    fonts-noto-unhinted \
    # Additional font families for maximum compatibility
    fonts-liberation \
    fonts-liberation2 \
    fonts-dejavu \
    fonts-dejavu-core \
    fonts-dejavu-extra \
    # Rebuild font cache for all installed fonts
    && fc-cache -fv

# RUN curl -L -o /usr/share/fonts/noto/NotoSansEthiopic-Regular.ttf https://github.com/googlefonts/noto-fonts/raw/main/hinted/ttf/NotoSansEthiopic/NotoSansEthiopic-Regular.ttf
# Set working directory
WORKDIR /data


RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

COPY main.py /data/main.py
COPY header.tex /data/header.tex

# Default command
# CMD ["pandoc", "--version"]
CMD ["tail", "-f", "/dev/null"]
