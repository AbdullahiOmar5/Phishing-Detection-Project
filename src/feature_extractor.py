import re
from urllib.parse import urlparse

def extract_features_from_url(url: str) -> dict:
    """
    Extracts key phishing-related features from a URL.
    Returns a dict of top 20 features your trained model uses.
    """
    parsed = urlparse(url)
    hostname = parsed.hostname or ""
    path = parsed.path or ""

    # Basic parts
    url_length = len(url)
    hostname_length = len(hostname)
    nb_dots = hostname.count(".")
    nb_hyphens = hostname.count("-")
    nb_at = url.count("@")
    nb_subdomains = len(hostname.split(".")) - 2 if hostname.count(".") > 1 else 0

    # Ratios
    digits_url = len(re.findall(r"\d", url))
    digits_host = len(re.findall(r"\d", hostname))
    ratio_digits_url = digits_url / len(url) if len(url) > 0 else 0
    ratio_digits_host = digits_host / len(hostname) if len(hostname) > 0 else 0

    # Path analysis
    path_segments = path.split("/")
    words = [seg for seg in path_segments if seg]
    word_lengths = [len(w) for w in words] if words else [0]
    avg_words_raw = sum(word_lengths) / len(word_lengths) if words else 0
    longest_words_raw = max(word_lengths) if words else 0
    shortest_words_raw = min(word_lengths) if words else 0

    # Binary features
    prefix_suffix = 1 if "-" in hostname else 0
    random_domain = 1 if re.search(r"[a-zA-Z]{3,}\d{3,}", hostname) else 0
    shortening_service = 1 if re.search(r"bit\.ly|goo\.gl|tinyurl|is\.gd", url) else 0
    tld_in_path = 1 if re.search(r"\.(com|net|org|info|biz|xyz)", path) else 0
    abnormal_subdomain = 1 if nb_subdomains >= 3 else 0

    # Some structural placeholders
    path_extension = 1 if "." in path.split("/")[-1] else 0
    nb_redirection = url.count("//") - 1
    ratio_extHyperlinks = 0.0
    ratio_intErrors = 0.0

    # Return only model-used features (top 20)
    features = {
        "length_url": url_length,
        "length_hostname": hostname_length,
        "nb_dots": nb_dots,
        "nb_hyphens": nb_hyphens,
        "nb_at": nb_at,
        "ratio_digits_url": ratio_digits_url,
        "ratio_digits_host": ratio_digits_host,
        "shortest_words_raw": shortest_words_raw,
        "longest_words_raw": longest_words_raw,
        "avg_words_raw": avg_words_raw,
        "tld_in_path": tld_in_path,
        "abnormal_subdomain": abnormal_subdomain,
        "nb_subdomains": nb_subdomains,
        "prefix_suffix": prefix_suffix,
        "random_domain": random_domain,
        "shortening_service": shortening_service,
        "path_extension": path_extension,
        "nb_redirection": nb_redirection,
        "ratio_extHyperlinks": ratio_extHyperlinks,
        "ratio_intErrors": ratio_intErrors
    }

    return features
