#!/usr/bin/env python3
import json
import urllib.parse

def format_query_for_display(query):
    """Format query for display in the README."""
    if not query.strip():
        return "```dsl\n\n```"
    
    # Ensure proper formatting with triple backticks
    return f"```dsl\n{query}\n```"

def create_url_for_query(query, virtual_hosts=False):
    """Create a URL-encoded query for Censys search."""
    encoded_query = urllib.parse.quote_plus(query)
    base_url = "https://search.censys.io/search?resource=hosts"
    
    # Add virtual_hosts parameter if needed
    if virtual_hosts:
        return f"{base_url}&virtual_hosts=INCLUDE&q={encoded_query}&ref=awesome-censys-queries"
    else:
        return f"{base_url}&q={encoded_query}&ref=awesome-censys-queries"

def format_references(references):
    """Format references as a list for the README."""
    if not references:
        return ""
    
    ref_str = "<details>\n    <summary markdown=\"span\">References</summary>\n\n"
    for ref in references:
        ref_str += f"- <{ref}>\n"
    ref_str += "\n</details>"
    return ref_str

def format_notes(notes):
    """Format additional notes for the README."""
    if not notes:
        return ""
    
    return "\n".join(notes)

def format_screenshot(screenshot):
    """Format a screenshot detail section for the README."""
    if not screenshot:
        return ""
    
    alt_text = screenshot.split("/")[-1].split(".")[0]
    return f"<details>\n    <summary markdown=\"span\">Screenshot</summary>\n    <img src=\"{screenshot}\" alt=\"{alt_text}\" width=\"500px\" />\n</details>"

def generate_readme():
    """Generate the README.md content from queries.json."""
    with open('queries.json') as f:
        data = json.load(f)
    
    # Start with the header content
    readme = """# Awesome Censys Queries

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/thehappydinoa/awesome-censys-queries/main.svg)](https://results.pre-commit.ci/latest/github/thehappydinoa/awesome-censys-queries/main)
[![GitHub contributors](https://img.shields.io/github/contributors/thehappydinoa/awesome-censys-queries)](https://github.com/thehappydinoa/awesome-censys-queries/graphs/contributors)
[![GitHub Repo stars](https://img.shields.io/github/stars/thehappydinoa/awesome-censys-queries)](https://github.com/thehappydinoa/awesome-censys-queries/stargazers)
[![License](https://img.shields.io/github/license/thehappydinoa/awesome-censys-queries)](#license)
![Twitter URL](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fthehappydinoa%2Fawesome-censys-queries)

A collection of fascinating and bizarre [Censys Search](https://search.censys.io?ref=awesome-censys-queries) queries.

<!-- markdownlint-disable MD033 -->
<p align="center">
    <img src="./images/search.censys.io.png" alt="Censys Search" width="500px" />
</p>

## Contributing

Found an awesome query? [Submit it here](https://github.com/thehappydinoa/awesome-censys-queries/issues/new?assignees=thehappydinoa&labels=query+submissions&template=query-submission.md&title=)

Interested in contributing in another way? [See the contributing guidelines](CONTRIBUTING.md)

## Resources

- [Censys Search](https://search.censys.io?ref=awesome-censys-queries)
- [CensysGPT Beta - AI Generated Queries](https://gpt.censys.io?utm_source=github&utm_medium=awesome-censys-queries&utm_campaign=awesome-censys-queries)

## Key

- <a>🔎 &#x2192;</a> - This icon will take you to the Censys Search results page for the query.

## Table of Contents

<!-- markdownlint-disable MD004 MD005 MD007 MD032 -->

<!-- toc -->

"""
    
    # Generate the table of contents
    for category in data['categories']:
        readme += f"  * [{category['name']}](#{category['name'].lower().replace(' ', '-')})\n"
    
    readme += """- [Credits](#credits)
- [License](#license)
- [Star History](#star-history)

<!-- tocstop -->

<!-- markdownlint-enable MD004 MD005 MD007 MD032 -->

"""
    
    # Generate content for each category
    for category in data['categories']:
        readme += f"### {category['name']}\n\n"
        
        for query in category['queries']:
            # Create the encoded URL for the query
            virtual_hosts = query.get('virtual_hosts', False)
            url = create_url_for_query(query['query'], virtual_hosts)
            
            # Add the query section
            readme += f"#### {query['title']} [🔎 &#x2192;]({url})\n\n"
            readme += format_query_for_display(query['query']) + "\n\n"
            
            # Add notes if present
            if query.get('notes'):
                notes = [note for note in query.get('notes') if note]  # Filter out empty notes
                for i, note in enumerate(notes):
                    readme += f"> {note}"
                    # If it's the last note or the only note, add double newline
                    # Otherwise, add single newline between notes
                    if i == len(notes) - 1:
                        readme += "\n\n"  # Double newline after last note
                    else:
                        readme += "\n"  # Single newline between notes
            
            # Add screenshot if present
            if query.get('screenshot'):
                readme += format_screenshot(query['screenshot']) + "\n\n"
            
            # Add references if present
            if query.get('references'):
                readme += format_references(query['references']) + "\n\n"
    
    # Add credits section
    readme += "## Credits\n\n"
    for i, credit in enumerate(data['metadata']['credits']):
        url = data['metadata']['credit_urls'][i] if i < len(data['metadata']['credit_urls']) else ""
        if url:
            readme += f"- [{credit}]({url})\n"
        else:
            readme += f"- {credit}\n"
    
    # Add license and star history sections
    readme += """
## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=thehappydinoa/awesome-censys-queries&type=Date)](https://star-history.com/#thehappydinoa/awesome-censys-queries&Date)
"""
    
    # Write the README content to a file
    with open('README.md', 'w') as f:
        f.write(readme)
    
    print("README.md generated successfully!")

if __name__ == "__main__":
    generate_readme() 