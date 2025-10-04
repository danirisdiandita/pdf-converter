# Use Alpine Linux for minimal image size
FROM alpine:3.19

# Install Pandoc, LaTeX, and fonts for multilingual support
RUN apk add --no-cache \
    pandoc \
    texlive \
    texlive-xetex \
    texmf-dist-fontsextra \
    # Fonts for Latin, Cyrillic, Greek scripts
    font-noto \
    font-noto-extra \
    # CJK (Chinese, Japanese, Korean) fonts
    font-noto-cjk \
    # Arabic, Hebrew, and other scripts
    font-noto-arabic \
    font-noto-devanagari \
    font-noto-thai \
    # Additional language support
    font-liberation \
    fontconfig \
    && fc-cache -fv

# Set working directory
WORKDIR /data

# Default command
CMD ["pandoc", "--version"]
