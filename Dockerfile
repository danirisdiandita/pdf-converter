# Use Alpine Linux for minimal image size
FROM alpine:3.19

# Install Pandoc, LaTeX (full), and comprehensive font support for ALL languages
RUN apk add --no-cache \
    pandoc \
    texlive-full \
    # Install ALL Noto fonts for comprehensive Unicode coverage
    # This covers 1000+ languages and all major scripts
    font-noto \
    font-noto-extra \
    font-noto-cjk \
    font-noto-arabic \
    font-noto-hebrew \
    font-noto-armenian \
    font-noto-devanagari \
    font-noto-bengali \
    font-noto-tamil \
    font-noto-telugu \
    font-noto-malayalam \
    font-noto-kannada \
    font-noto-thai \
    font-noto-lao \
    font-noto-khmer \
    font-noto-myanmar \
    font-noto-sinhala \
    font-noto-georgian \
    font-noto-emoji \
    # Additional font families for maximum compatibility
    font-liberation \
    font-dejavu \
    fontconfig \
    # Rebuild font cache for all installed fonts
    && fc-cache -fv

# Set working directory
WORKDIR /data


RUN apk add --no-cache python3 py3-pip
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

RUN pip install --upgrade pip setuptools

COPY main.py /data/main.py
COPY header.tex /data/header.tex

# Default command
# CMD ["pandoc", "--version"]
CMD ["tail", "-f", "/dev/null"]
