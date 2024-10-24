from typing import Optional
from urllib.parse import quote_plus

from fasthtml.components import H1, H2, Div, Form, Img, NotStr, P, Span
from fasthtml.xtend import A, Script
from lucide_fasthtml import Lucide
from shad4fast import Badge, Button, Input, Label, RadioGroup, RadioGroupItem

# JavaScript to check the input value and enable/disable the search button and radio buttons
check_input_script = Script(
    """
        window.onload = function() {
            const input = document.getElementById('search-input');
            const button = document.querySelector('[data-button="search-button"]');
            const radioGroupItems = document.querySelectorAll('button[data-ref="radio-item"]');  // Get all radio buttons
            
            function checkInputValue() {
                const isInputEmpty = input.value.trim() === "";
                button.disabled = isInputEmpty;  // Disable the submit button
                radioGroupItems.forEach(item => {
                    item.disabled = isInputEmpty;  // Disable/enable the radio buttons
                });
            }

            input.addEventListener('input', checkInputValue);  // Listen for input changes
            checkInputValue();  // Initial check when the page loads
        };
    """
)

# JavaScript to handle the image swapping, reset button, and active class toggling
image_swapping = Script(
    """
    document.addEventListener('click', function (e) {
        if (e.target.classList.contains('sim-map-button') || e.target.classList.contains('reset-button')) {
            const imgContainer = e.target.closest('.relative'); 
            const overlayContainer = imgContainer.querySelector('.overlay-container');
            const newSrc = e.target.getAttribute('data-image-src');
    
            // If it's a reset button, remove the overlay image
            if (e.target.classList.contains('reset-button')) {
                overlayContainer.innerHTML = '';  // Clear the overlay container, showing only the full image
            } else {
                // Create a new overlay image
                const img = document.createElement('img');
                img.src = newSrc;
                img.classList.add('overlay-image', 'absolute', 'top-0', 'left-0', 'w-full', 'h-full');
                overlayContainer.innerHTML = '';  // Clear any previous overlay
                overlayContainer.appendChild(img);  // Add the new overlay image
            }
    
            // Toggle active class on buttons
            const activeButton = document.querySelector('.sim-map-button.active');
            if (activeButton) {
                activeButton.classList.remove('active');
            }
            if (e.target.classList.contains('sim-map-button')) {
                e.target.classList.add('active');
            }
        }
    });
    """
)

toggle_text_content = Script(
    """
    function toggleTextContent(idx) {
        const textColumn = document.getElementById(`text-column-${idx}`);
        const imageTextColumns = document.getElementById(`image-text-columns-${idx}`);
        const toggleButton = document.getElementById(`toggle-button-${idx}`);
    
        if (textColumn.classList.contains('md-grid-text-column')) {
          // Hide the text column
          textColumn.classList.remove('md-grid-text-column');
          imageTextColumns.classList.remove('grid-image-text-columns');
          toggleButton.innerText = `Show Text`;
        } else {
          // Show the text column
          textColumn.classList.add('md-grid-text-column');
          imageTextColumns.classList.add('grid-image-text-columns');
          toggleButton.innerText = `Hide Text`;
        }
    }
    """
)


def SearchBox(with_border=False, query_value="", ranking_value="nn+colpali"):
    grid_cls = "grid gap-2 items-center p-3 bg-muted/80 dark:bg-muted/40 w-full"

    if with_border:
        grid_cls = "grid gap-2 p-3 rounded-md border border-input bg-muted/80 dark:bg-muted/40 w-full ring-offset-background focus-within:outline-none focus-within:ring-2 focus-within:ring-ring focus-within:ring-offset-2 focus-within:border-input"

    return Form(
        Div(
            Lucide(icon="search", cls="absolute left-2 top-2 text-muted-foreground"),
            Input(
                placeholder="Enter your search query...",
                name="query",
                value=query_value,
                id="search-input",
                cls="text-base pl-10 border-transparent ring-offset-transparent ring-0 focus-visible:ring-transparent",
                style="font-size: 1rem",
                autofocus=True,
            ),
            cls="relative",
        ),
        Div(
            Div(
                Span("Ranking by:", cls="text-muted-foreground text-xs font-semibold"),
                RadioGroup(
                    Div(
                        RadioGroupItem(value="nn+colpali", id="nn+colpali"),
                        Label("nn+colpali", htmlFor="nn+colpali"),
                        cls="flex items-center space-x-2",
                    ),
                    Div(
                        RadioGroupItem(value="bm25+colpali", id="bm25+colpali"),
                        Label("bm25+colpali", htmlFor="bm25+colpali"),
                        cls="flex items-center space-x-2",
                    ),
                    Div(
                        RadioGroupItem(value="bm25", id="bm25"),
                        Label("bm25", htmlFor="bm25"),
                        cls="flex items-center space-x-2",
                    ),
                    name="ranking",
                    default_value=ranking_value,
                    cls="grid-flow-col gap-x-5 text-muted-foreground",
                ),
                cls="grid grid-flow-col items-center gap-x-3 border border-input px-3 rounded-sm",
            ),
            Button(
                Lucide(icon="arrow-right", size="21"),
                size="sm",
                type="submit",
                data_button="search-button",
                disabled=True,
            ),
            cls="flex justify-between",
        ),
        check_input_script,
        action=f"/search?query={quote_plus(query_value)}&ranking={quote_plus(ranking_value)}",
        method="GET",
        hx_get=f"/fetch_results?query={quote_plus(query_value)}&ranking={quote_plus(ranking_value)}",
        hx_trigger="load",
        hx_target="#search-results",
        hx_swap="outerHTML",
        hx_indicator="#loading-indicator",
        cls=grid_cls,
    )


def SampleQueries():
    sample_queries = [
        "Total amount of fixed salaries paid in 2023?",
        "Proportion of female new hires 2021-2023?",
        "Value of unlisted real estate 2023?",
        "Fund currency basket returns 2023",
        "Employees per office site?",
    ]

    query_badges = []
    for query in sample_queries:
        query_badges.append(
            A(
                Badge(
                    Div(
                        Lucide(
                            icon="text-search", size="18", cls="text-muted-foreground"
                        ),
                        Span(query, cls="text-base font-normal"),
                        cls="flex gap-2 items-center",
                    ),
                    variant="outline",
                    cls="text-base font-normal text-muted-foreground hover:border-black dark:hover:border-white",
                ),
                href=f"/search?query={quote_plus(query)}",
                cls="no-underline",
            )
        )

    return Div(*query_badges, cls="grid gap-2 justify-items-center")


def Hero():
    return Div(
        H1(
            "Vespa.ai + ColPali",
            cls="text-5xl md:text-7xl font-bold tracking-wide md:tracking-wider bg-clip-text text-transparent bg-gradient-to-r from-black to-gray-700 dark:from-white dark:to-gray-300 animate-fade-in",
        ),
        P(
            "Efficient Document Retrieval with Vision Language Models",
            cls="text-lg md:text-2xl text-muted-foreground md:tracking-wide",
        ),
        cls="grid gap-5 text-center",
    )


def Home():
    return Div(
        Div(
            Hero(),
            SearchBox(with_border=True),
            SampleQueries(),
            cls="grid gap-8 -mt-[21vh]",
        ),
        cls="grid w-full h-full max-w-screen-md items-center gap-4 mx-auto",
    )


def Search(request, search_results=[]):
    query_value = request.query_params.get("query", "").strip()
    ranking_value = request.query_params.get("ranking", "nn+colpali")
    print(
        f"Search: Fetching results for query: {query_value}, ranking: {ranking_value}"
    )
    return Div(
        Div(
            Div(
                SearchBox(query_value=query_value, ranking_value=ranking_value),
                Div(
                    LoadingMessage(),
                    id="search-results",  # This will be replaced by the search results
                ),
                cls="grid",
            ),
            cls="grid",
        ),
    )


def LoadingMessage(display_text="Retrieving search results"):
    return Div(
        Lucide(icon="loader-circle", cls="size-5 mr-1.5 animate-spin"),
        Span(display_text, cls="text-base text-center"),
        cls="p-10 text-muted-foreground flex items-center justify-center",
        id="loading-indicator",
    )


def LoadingSkeleton():
    return Div(
        Div(cls="h-5 bg-muted"),
        Div(cls="h-5 bg-muted"),
        Div(cls="h-5 bg-muted"),
        cls="grid gap-2 animate-pulse",
    )


def SimMapButtonReady(query_id, idx, token, img_src):
    return Button(
        token,
        size="sm",
        data_image_src=img_src,
        id=f"sim-map-button-{query_id}-{idx}-{token}",
        cls="sim-map-button pointer-events-auto font-mono text-xs h-5 rounded-none px-2",
    )


def SimMapButtonPoll(query_id, idx, token):
    return Button(
        Lucide(icon="loader-circle", size="15", cls="animate-spin"),
        size="sm",
        disabled=True,
        hx_get=f"/get_sim_map?query_id={query_id}&idx={idx}&token={token}",
        # Poll every x seconds, where x is 0.3 x idx, formatted to 2 decimals
        hx_trigger=f"every {(idx+1)*0.3:.2f}s",
        hx_swap="outerHTML",
        cls="pointer-events-auto text-xs h-5 rounded-none px-2",
    )


def SearchResult(results: list, query_id: Optional[str] = None):
    if not results:
        return Div(
            P(
                "No results found for your query.",
                cls="text-muted-foreground text-base text-center",
            ),
            cls="grid p-10",
        )

    # Otherwise, display the search results
    result_items = []
    for idx, result in enumerate(results):
        fields = result["fields"]  # Extract the 'fields' part of each result
        blur_image_base64 = f"data:image/jpeg;base64,{fields['blur_image']}"

        # Filter sim_map fields that are words with 4 or more characters
        sim_map_fields = {
            key: value
            for key, value in fields.items()
            if key.startswith(
                "sim_map_"
            )  # filtering is done before creating with 'is_special_token'-function
        }

        # Generate buttons for the sim_map fields
        sim_map_buttons = []
        for key, value in sim_map_fields.items():
            if value is not None:
                sim_map_base64 = f"data:image/jpeg;base64,{value}"
                sim_map_buttons.append(
                    SimMapButtonReady(
                        query_id=query_id,
                        idx=idx,
                        token=key.split("_")[-1],
                        img_src=sim_map_base64,
                    )
                )
            else:
                sim_map_buttons.append(
                    SimMapButtonPoll(
                        query_id=query_id, idx=idx, token=key.split("_")[-1]
                    )
                )

        # Add "Reset Image" button to restore the full image
        reset_button = Button(
            "Reset",
            variant="outline",
            size="sm",
            data_image_src=blur_image_base64,
            cls="reset-button pointer-events-auto font-mono text-xs h-5 rounded-none px-2",
        )

        tokens_icon = Lucide(icon="images", size="15")

        # Add "Tokens" button - this has no action, just a placeholder
        tokens_button = Button(
            tokens_icon,
            "Tokens",
            size="sm",
            cls="tokens-button flex gap-[3px] font-bold pointer-events-none font-mono text-xs h-5 rounded-none px-2",
        )

        result_items.append(
            Div(
                Div(
                    Div(
                        Lucide(icon="file-text"),
                        H2(fields["title"], cls="text-xl md:text-2xl font-semibold"),
                        cls="flex items-center gap-2",
                    ),
                    Div(
                        Button(
                            "Show Text",
                            size="sm",
                            id=f"toggle-button-{idx}",
                            onclick=f"toggleTextContent({idx})",
                        ),
                    ),
                    cls="flex flex-wrap items-center justify-between bg-background px-3 py-4",
                ),
                Div(
                    Div(
                        Div(
                            tokens_button,
                            *sim_map_buttons,
                            reset_button,
                            cls="flex flex-wrap gap-px w-full pointer-events-none",
                        ),
                        Div(
                            Div(
                                Div(
                                    Img(
                                        src=blur_image_base64,
                                        hx_get=f"/full_image?docid={fields['id']}&query_id={query_id}&idx={idx}",
                                        style="backdrop-filter: blur(5px);",
                                        hx_trigger="load",
                                        hx_swap="outerHTML",
                                        alt=fields["title"],
                                        cls="result-image w-full h-full object-contain",
                                    ),
                                    Div(
                                        cls="overlay-container absolute top-0 left-0 w-full h-full pointer-events-none"
                                    ),
                                    cls="relative w-full h-full",
                                ),
                                cls="grid bg-border p-2",
                            ),
                            cls="block",
                        ),
                        id=f"image-column-{idx}",
                        cls="image-column relative bg-background px-3 py-5 grid-image-column",
                    ),
                    Div(
                        Div(
                            P(
                                "Page " + str(fields["page_number"]),
                                cls="text-foreground font-mono bold text-sm",
                            ),
                            Badge(
                                f"Relevance score: {result['relevance']:.4f}",
                                cls="flex gap-1.5 items-center justify-center",
                            ),
                            cls="flex items-center justify-between",
                        ),
                        Div(
                            Div(
                                Div(
                                    P(
                                        NotStr(fields.get("snippet", "")),
                                        cls="text-highlight text-muted-foreground",
                                    ),
                                    P(
                                        NotStr(fields.get("text", "")),
                                        cls="text-highlight text-muted-foreground",
                                    ),
                                    cls="grid gap-y-3 p-5 text-sm",
                                ),
                                cls="grid bg-background content-start ",
                            ),
                            cls="grid bg-border p-2",
                        ),
                        id=f"text-column-{idx}",
                        cls="text-column relative bg-background px-3 py-5 hidden",
                    ),
                    id=f"image-text-columns-{idx}",
                    cls="relative grid grid-cols-1 border-t",
                ),
                cls="grid grid-cols-1 grid-rows-[auto_1fr]",
            ),
        )

    return Div(
        *result_items,
        image_swapping,
        toggle_text_content,
        id="search-results",
        cls="grid grid-cols-1 gap-px bg-border",
    )


def ChatResult(query_id: str, query: str):
    return Div(
        Div("LLM Response", cls="text-xl font-semibold p-3"),
        Div(
            Div(
                Div(
                    LoadingSkeleton(),
                    hx_ext="sse",
                    sse_connect=f"/get-message?query_id={query_id}&query={quote_plus(query)}",
                    sse_swap="message",
                    sse_close="close",
                    hx_swap="innerHTML",
                ),
            ),
            id="chat-messages",
            cls="overflow-auto min-h-0 grid items-end px-3",
        ),
        cls="h-full grid grid-rows-[auto_1fr_auto] min-h-0 gap-3",
    )
