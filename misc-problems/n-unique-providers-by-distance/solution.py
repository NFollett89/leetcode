#!/usr/bin/env python3

def spread_n_providers(sites: [map], N: int) -> [str]:
    sorted_sites = sorted(sites, key=lambda x: x["distance"])
    sites_by_provider = {}
    for site in sorted_sites:
        p = site["provider"]
        if not sites_by_provider.get(p):
            sites_by_provider[p] = []
        sites_by_provider[p].append(site)
    choices = []
    count = 0
    wrap_i = 0
    while count < N and count < len(sites):
        for p, s in sites_by_provider.items():
            if count == N:
                break
            try:
                choices.append(s[wrap_i]["name"])
                count += 1
            except:
                pass
        wrap_i += 1
    return choices

if __name__ == "__main__":
    sites = [
        {"name": "a", "provider": "aws", "distance": 100},
        {"name": "b", "provider": "gcp", "distance": 500},
        {"name": "c", "provider": "azure", "distance": 300},
        {"name": "d", "provider": "aws", "distance": 200},
        {"name": "e", "provider": "gcp", "distance": 250},
        {"name": "f", "provider": "aws", "distance": 150},
        {"name": "g", "provider": "azure", "distance": 350},
        {"name": "h", "provider": "aws", "distance": 400},
        {"name": "i", "provider": "gcp", "distance": 150},
    ]
    clouds = spread_n_providers(sites, 4)
    print(clouds == ['a', 'i', 'c', 'f'])
    clouds = spread_n_providers(sites, 1)
    print(clouds)
