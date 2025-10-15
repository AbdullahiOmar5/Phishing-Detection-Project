import re
from urllib.parse import urlparse

def extract_features_from_url_extended(url: str) -> dict:
    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    path = parsed.path or ""

    # Existing features
    url_length = len(url)
    hostname_length = len(hostname)
    nb_dots = hostname.count(".")
    nb_hyphens = hostname.count("-")
    nb_at = url.count("@")
    nb_subdomains = max(0, len(hostname.split(".")) - 2)
    digits_url = len(re.findall(r"\d", url))
    digits_host = len(re.findall(r"\d", hostname))
    ratio_digits_url = digits_url / url_length if url_length else 0
    ratio_digits_host = digits_host / hostname_length if hostname_length else 0
    segments = [seg for seg in path.split("/") if seg]
    lengths = [len(s) for s in segments] or [0]
    shortest_words_raw = min(lengths)
    longest_words_raw = max(lengths)
    avg_words_raw = sum(lengths) / len(lengths)
    prefix_suffix = int("-" in hostname)
    random_domain = int(bool(re.search(r"[a-zA-Z]{3,}\d{3,}", hostname)))
    shortening_service = int(bool(re.search(r"(bit\.ly|goo\.gl|tinyurl|is\.gd)", url, re.IGNORECASE)))
    tld_in_path = int(bool(re.search(r"\.(com|net|org|info|biz|xyz)", path, re.IGNORECASE)))
    abnormal_subdomain = int(nb_subdomains >= 3)
    path_extension = int("." in path.split("/")[-1])
    nb_redirection = max(0, url.count("//") - 1)

    # New features
    is_https = int(url.lower().startswith("https"))
    has_ip = int(bool(re.match(r"\d+\.\d+\.\d+\.\d+", hostname)))
    num_query_params = url.count("?") + url.count("&")
    num_special = sum(url.count(c) for c in ["@", "-", "_", "~", "!", "$"])
    suspicious_tld = int(bool(re.search(r"\.(xyz|top|info|club|gq|online)$", hostname, re.IGNORECASE)))

    # Combine all features
    features = {
        "length_url": float(url_length),
        "length_hostname": float(hostname_length),
        "nb_dots": float(nb_dots),
        "nb_hyphens": float(nb_hyphens),
        "nb_at": float(nb_at),
        "ratio_digits_url": float(ratio_digits_url),
        "ratio_digits_host": float(ratio_digits_host),
        "shortest_words_raw": float(shortest_words_raw),
        "longest_words_raw": float(longest_words_raw),
        "avg_words_raw": float(avg_words_raw),
        "tld_in_path": float(tld_in_path),
        "abnormal_subdomain": float(abnormal_subdomain),
        "nb_subdomains": float(nb_subdomains),
        "prefix_suffix": float(prefix_suffix),
        "random_domain": float(random_domain),
        "shortening_service": float(shortening_service),
        "path_extension": float(path_extension),
        "nb_redirection": float(nb_redirection),
        "ratio_extHyperlinks": 0.0,  # placeholder
        "ratio_intErrors": 0.0,      # placeholder
        "is_https": float(is_https),
        "has_ip": float(has_ip),
        "num_query_params": float(num_query_params),
        "num_special": float(num_special),
        "suspicious_tld": float(suspicious_tld)
    }

    return features
