import re

# List of supported URL schemes (protocols)
schemes = \
            [
                "http",       # Hypertext Transfer Protocol
                "https",      # Secure Hypertext Transfer Protocol
                "ftp",        # File Transfer Protocol
                "ftps",       # Secure File Transfer Protocol
                "sftp",       # SSH File Transfer Protocol
                "file",       # Local file access
                "mailto",     # Email links
                "data",       # Inline data
                "tel",        # Telephone links
                "sms",        # SMS links
                "ws",         # WebSockets
                "wss",        # Secure WebSockets
                "gopher",     # Gopher protocol (rarely used now)
                "irc",        # Internet Relay Chat
                "ircs",       # Secure Internet Relay Chat
                "xmpp",       # Extensible Messaging and Presence Protocol
                "ldap",       # Lightweight Directory Access Protocol
                "ldaps",      # Secure LDAP
                "bitcoin",    # Bitcoin payment links
                "geo",        # Geolocation
                "telnet",     # Telnet protocol
                "ssh",        # Secure Shell protocol
                "svn",        # Subversion protocol
                "nfs",        # Network File System
                "vnc",        # Virtual Network Computing
                "magnet",     # Magnet links (e.g., for torrent files)
                "sip",        # Session Initiation Protocol (VoIP)
                "sips",       # Secure Session Initiation Protocol
            ]

# List of common subdomains
subdomains = \
                [
                    "www",        # Main website
                    "mail",       # Email service
                    "blog",       # Blog section
                    "shop",       # E-commerce store
                    "forum",      # Discussion forums
                    "admin",      # Administrative dashboard
                    "dev",        # Development environment
                    "support",    # Customer support
                    "news",       # News-related content
                    "cdn",        # Content delivery network
                    "app",        # Hosted applications
                    "events",     # Event-related content
                    "docs",       # Documentation section
                ]

# List of generic top-level domains (TLDs)
generic_tlds = \
                [
                    "com",        # Commercial
                    "org",        # Organization
                    "net",        # Network
                    "edu",        # Educational institutions
                    "gov",        # Government
                    "mil",        # Military
                    "int",        # International organizations
                    "info",       # Information
                    "biz",        # Business
                    "name",       # Personal names
                    "pro",        # Professionals
                    "coop",       # Cooperatives
                    "museum",     # Museums
                    "aero",       # Aerospace industry
                    "jobs",       # Employment-related sites
                    "mobi",       # Mobile sites
                    "travel",     # Travel and tourism
                    "post",       # Postal services
                ]

# Create regular expressions by joining the lists with '|'
schemesRX = '|'.join(schemes)       # Supported schemes regex
subdomainsRX = '|'.join(subdomains) # Supported subdomains regex
generic_tldsRX = '|'.join(generic_tlds) # Supported TLDs regex

# Define a URL pattern using the compiled regex components
UrlPattern = re.compile(
    r"(?P<schemes>{}){}(://)(?P<subdomains>{})(\.)(\w+)(\.)(?P<generic_tlds>{})".format(
        schemesRX, "{1}", subdomainsRX, generic_tldsRX
    )
)

# Test input with valid and invalid URLs
Test = """Valid URLs:
            http
            httphttphttp
            https://www.Google.edu
            https://app.example.org
            http://example.com
            https://subdomain.example.com
            http://example.com/path/to/page
            https://www.example.com:8080
            ftp://ftp.example.com
            http://example.com/path?query=1&other=2
            https://mail.example.com/#fragment
            https://username:password@www.example.com
            http://docs.example.com:443/path?query=value#fragment
            Invalid URLs:

            htp://www.example.com (misspelled protocol)
            https:// (missing domain)
            www.example.com (missing protocol)
            http://example (missing domain or TLD)
            http://192.168.1.1 (valid IP but needs validation based on your use case)
            ://example.com (missing protocol)
            https://path/to/page (missing domain)
            Edge Cases:

            http://localhost
            http://127.0.0.1:8000
            https://subdomain.example.com:443/path?query=value
            http://example.com:99999 (port number out of range)
            http://example.com/path/with/multiple/segments"""

# Find all matches in the test input
result = re.findall(UrlPattern, Test)

# Print each matched URL component
for url in result:
    for part in url:
        print(part, end="")
    print()
