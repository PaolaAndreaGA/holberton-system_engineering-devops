# Query string

From Wikipedia, the free encyclopedia

[Jump to navigation](https://en.wikipedia.org/wiki/Query_string#mw-head)[Jump to search](https://en.wikipedia.org/wiki/Query_string#searchInput)

A  **query string**  is a part of a  [uniform resource locator](https://en.wikipedia.org/wiki/Uniform_resource_locator "Uniform resource locator")  (URL) that assigns values to specified parameters. A query string commonly includes fields added to a base URL by a Web browser or other client application, for example as part of an HTML, choosing the appearance of a page, or jumping to positions in multimedia content.[[1]](https://en.wikipedia.org/wiki/Query_string#cite_note-html5-1)[[2]](https://en.wikipedia.org/wiki/Query_string#cite_note-2)[[3]](https://en.wikipedia.org/wiki/Query_string#cite_note-3)

[![](https://upload.wikimedia.org/wikipedia/commons/0/06/Query_string.png)](https://en.wikipedia.org/wiki/File:Query_string.png)

An  [address bar](https://en.wikipedia.org/wiki/Address_bar "Address bar")  on  [Google Chrome](https://en.wikipedia.org/wiki/Google_Chrome "Google Chrome")  showing a  [URL](https://en.wikipedia.org/wiki/URL "URL")  with the query string  `title=Query_string&action=edit`.

A web server can handle a  [Hypertext Transfer Protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol "Hypertext Transfer Protocol")  (HTTP) request either by reading a file from its  [file system](https://en.wikipedia.org/wiki/File_system "File system")  based on the  [URL](https://en.wikipedia.org/wiki/Uniform_Resource_Locator "Uniform Resource Locator")  path or by handling the request using logic that is specific to the type of resource. In cases where special logic is invoked, the query string will be available to that logic for use in its processing, along with the path component of the URL.

## Contents

-   [1Structure](https://en.wikipedia.org/wiki/Query_string#Structure)
    -   [1.1Web forms](https://en.wikipedia.org/wiki/Query_string#Web_forms)
        -   [1.2Indexed search](https://en.wikipedia.org/wiki/Query_string#Indexed_search)
	-   [2URL encoding](https://en.wikipedia.org/wiki/Query_string#URL_encoding)
	-   [3Example](https://en.wikipedia.org/wiki/Query_string#Example)
	-   [4Tracking](https://en.wikipedia.org/wiki/Query_string#Tracking)
	-   [5Compatibility  issues](https://en.wikipedia.org/wiki/Query_string#Compatibility_issues)
	-   [6See also](https://en.wikipedia.org/wiki/Query_string#See_also)
	-   [7References](https://en.wikipedia.org/wiki/Query_string#References)

## Structure[[edit](https://en.wikipedia.org/w/index.php?title=Query_string&action=edit&section=1 "Edit section: Structure")]

Typical URL containing a query string is as follows:

> `https://example.com/over/there?name=ferret`

When a server receives a request for such a page, it may run a program, passing the query string, which in this case is  `name=ferret`, unchanged to the program. The question mark is used as a separator, and is not part of the query string.[[4]](https://en.wikipedia.org/wiki/Query_string#cite_note-4)[[5]](https://en.wikipedia.org/wiki/Query_string#cite_note-5)

[Web frameworks](https://en.wikipedia.org/wiki/Web_Framework "Web Framework")  may provide methods for parsing multiple parameters in the query string, separated by some delimiter.[[6]](https://en.wikipedia.org/wiki/Query_string#cite_note-w3c-recom-6)  In the example URL below, multiple query parameters are separated by the  [ampersand](https://en.wikipedia.org/wiki/Ampersand "Ampersand"), "`&`":

> `https://example.com/path/to/page?name=ferret&color=purple`

The exact structure of the query string is not standardized. Methods used to parse the query string may differ between websites.

A link in a web page may have a URL that contains a query string.  [HTML](https://en.wikipedia.org/wiki/HTML "HTML")  defines three ways a user agent can generate the query string:

-   an  [HTML form](https://en.wikipedia.org/wiki/Form_(HTML) "Form (HTML)")  via the  `<form>...</form>`  element
-   a  [server-side image map](https://en.wikipedia.org/wiki/Image_map#Server-side "Image map")  via the  `ismap`  attribute on the  `<img>`  element with an  `<img ismap>`  construction
-   an indexed search via the now deprecated  `<isindex>`  element

### Web forms[[edit](https://en.wikipedia.org/w/index.php?title=Query_string&action=edit&section=2 "Edit section: Web forms")]

One of the original uses was to contain the content of an  [HTML form](https://en.wikipedia.org/wiki/Form_(HTML) "Form (HTML)"), also known as web form. In particular, when a form containing the fields  `field1`,  `field2`,  `field3`  is submitted, the content of the fields is encoded as a query string as follows:

> `field1=value1&field2=value2&field3=value3...`

-   The query string is composed of a series of field-value pairs.
-   Within each pair, the field name and value are separated by an  [equals sign](https://en.wikipedia.org/wiki/Equals_sign "Equals sign"), "`=`".
-   The series of pairs is separated by the  [ampersand](https://en.wikipedia.org/wiki/Ampersand "Ampersand"), "`&`" (or  [semicolon](https://en.wikipedia.org/wiki/Semicolon "Semicolon"), "`;`" for URLs embedded in HTML and not generated by a  `<form>...</form>`. See below).

While there is no definitive standard, most  [web frameworks](https://en.wikipedia.org/wiki/Web_framework "Web framework")  allow multiple values to be associated with a single field (e.g.  `field1=value1&field1=value2&field2=value3`).[[7]](https://en.wikipedia.org/wiki/Query_string#cite_note-7)[[8]](https://en.wikipedia.org/wiki/Query_string#cite_note-8)

For each  [field](https://en.wikipedia.org/wiki/Field_(computer_science) "Field (computer science)")  of the form, the query string contains a pair  `field=value`. Web forms may include fields that are not visible to the user; these fields are included in the query string when the form is submitted.

This convention is a  [W3C](https://en.wikipedia.org/wiki/W3C "W3C")  recommendation.[[6]](https://en.wikipedia.org/wiki/Query_string#cite_note-w3c-recom-6)  W3C recommends that all web servers support  [semicolon](https://en.wikipedia.org/wiki/Semicolon "Semicolon")  separators in addition to  [ampersand](https://en.wikipedia.org/wiki/Ampersand "Ampersand")  separators[[9]](https://en.wikipedia.org/wiki/Query_string#cite_note-9)  to allow  [application/x-www-form-urlencoded](https://en.wikipedia.org/wiki/Application/x-www-form-urlencoded "Application/x-www-form-urlencoded")  query strings in URLs within HTML documents without having to entity escape ampersands.

The form content is only encoded in the URL's query string when the form submission method is  [GET](https://en.wikipedia.org/wiki/GET_(HTTP) "GET (HTTP)"). The same encoding is used by default when the submission method is  [POST](https://en.wikipedia.org/wiki/POST_(HTTP) "POST (HTTP)"), but the result is submitted as the  [HTTP request](https://en.wikipedia.org/wiki/HTTP_request "HTTP request")  body rather than being included in a modified URL.[[1]](https://en.wikipedia.org/wiki/Query_string#cite_note-html5-1)

### Indexed search[[edit](https://en.wikipedia.org/w/index.php?title=Query_string&action=edit&section=3 "Edit section: Indexed search")]

Before  [forms](https://en.wikipedia.org/wiki/Form_(HTML) "Form (HTML)")  were added to HTML, browsers rendered the  `<isindex>`  element as a single-line text-input control. The text entered into this control was sent to the server as a query string addition to a  [GET](https://en.wikipedia.org/wiki/GET_(HTTP) "GET (HTTP)")  request for the base URL or another URL specified by the  `action`  attribute.[[10]](https://en.wikipedia.org/wiki/Query_string#cite_note-10)  This was intended to allow web servers to use the provided text as query criteria so they could return a list of matching pages.[[11]](https://en.wikipedia.org/wiki/Query_string#cite_note-11)

When the text input into the indexed search control is submitted, it is encoded as a query string as follows:

> `argument1+argument2+argument3...`

-   The query string is composed of a series of arguments by parsing the text into words at the spaces.
-   The series is separated by the  [plus sign](https://en.wikipedia.org/wiki/Plus_sign "Plus sign"), '`+`'.

Though the  `<isindex>`  element is deprecated and most browsers no longer support or render it, there are still some vestiges of indexed search in existence. For example, this is the source of the special handling of  [plus sign](https://en.wikipedia.org/wiki/Plus_sign "Plus sign"), '`+`' within browser URL percent encoding (which today, with the deprecation of indexed search, is all but redundant with  `%20`). Also some web servers supporting  [CGI](https://en.wikipedia.org/wiki/Common_Gateway_Interface "Common Gateway Interface")  (e.g.,  [Apache](https://en.wikipedia.org/wiki/Apache_HTTP_Server "Apache HTTP Server")) will process the query string into command line arguments if it does not contain an  [equals sign](https://en.wikipedia.org/wiki/Equals_sign "Equals sign"), '`=`' (as per section 4.4 of CGI 1.1). Some CGI scripts still depend on and use this historic behavior for URLs embedded in HTML.

## URL encoding[[edit](https://en.wikipedia.org/w/index.php?title=Query_string&action=edit&section=4 "Edit section: URL encoding")]

Main article:  [Percent-encoding](https://en.wikipedia.org/wiki/Percent-encoding "Percent-encoding")

Some  [characters](https://en.wikipedia.org/wiki/Character_(computing) "Character (computing)")  cannot be part of a URL (for example, the space) and some other characters have a special meaning in a URL: for example, the character  `#`  can be used to further specify a subsection (or  [fragment](https://en.wikipedia.org/wiki/Fragment_identifier "Fragment identifier")) of a document. In HTML forms, the character  `=`  is used to separate a name from a value. The URI generic syntax uses  [URL encoding](https://en.wikipedia.org/wiki/Percent-encoding#Percent-encoding_reserved_characters "Percent-encoding")  to deal with this problem, while HTML forms make some additional substitutions rather than applying percent encoding for all such characters. SPACE is encoded as '`+`' or "`%20`".[[12]](https://en.wikipedia.org/wiki/Query_string#cite_note-w3schools-12)

[HTML 5](https://en.wikipedia.org/wiki/HTML_5 "HTML 5")  specifies the following transformation for submitting HTML forms with the "GET" method to a web server.[[1]](https://en.wikipedia.org/wiki/Query_string#cite_note-html5-1)  The following is a brief summary of the algorithm:

-   Characters that cannot be converted to the correct charset are replaced with HTML  [numeric character references](https://en.wikipedia.org/wiki/Numeric_character_reference "Numeric character reference")[[13]](https://en.wikipedia.org/wiki/Query_string#cite_note-html5_urlencoded-13)
-   SPACE is encoded as '`+`' or '`%20`'
-   Letters (`A`–`Z`  and  `a`–`z`), numbers (`0`–`9`) and the characters '`~`','`-`','`.`' and '`_`' are left as-is
-   `+`  is encoded by %2B
-   All other characters are encoded as a  `%HH`  [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal "Hexadecimal")  representation with any non-ASCII characters first encoded as UTF-8 (or other specified encoding)

The octet corresponding to the tilde ("`~`") is permitted in query strings by RFC3986 but required to be percent-encoded in HTML forms to "`%7E`".

The encoding of SPACE as '`+`' and the selection of "as-is" characters distinguishes this encoding from RFC 3986.

## Example[[edit](https://en.wikipedia.org/w/index.php?title=Query_string&action=edit&section=5 "Edit section: Example")]

If a  [form](https://en.wikipedia.org/wiki/Form_(web) "Form (web)")  is embedded in an  [HTML](https://en.wikipedia.org/wiki/HTML "HTML")  page as follows:

<form action="/cgi-bin/test.cgi" method="get">
  <input type="text" name="first" />
    <input type="text" name="second" />
      <input type="submit" />
      </form>

and the user inserts the strings “this is a field” and “was it clear (already)?” in the two  [text fields](https://en.wikipedia.org/wiki/Text_box "Text box")  and presses the submit button, the program  `test.cgi`  (the program specified by the  `action`  [attribute](https://en.wikipedia.org/wiki/HTML_attribute "HTML attribute")  of the  `form`  [element](https://en.wikipedia.org/wiki/HTML_element "HTML element")  in the above example) will receive the following query string:  `first=this+is+a+field&second=was+it+clear+%28already%29%3F`.

If the form is processed on the  [server](https://en.wikipedia.org/wiki/Web_server "Web server")  by a  [CGI](https://en.wikipedia.org/wiki/Common_Gateway_Interface "Common Gateway Interface")  [script](https://en.wikipedia.org/wiki/Scripting_language "Scripting language"), the script may typically receive the query string as an  [environment variable](https://en.wikipedia.org/wiki/Environment_variable "Environment variable")  named  `QUERY_STRING`.

## Tracking[[edit](https://en.wikipedia.org/w/index.php?title=Query_string&action=edit&section=6 "Edit section: Tracking")]

A program receiving a query string can ignore part or all of it. If the requested URL corresponds to a file and not to a program, the whole query string is ignored. However, regardless of whether the query string is used or not, the whole URL including it is stored in the server  [log files](https://en.wikipedia.org/wiki/Computer_data_logging "Computer data logging").

These facts allow query strings to be used to track users in a manner similar to that provided by  [HTTP cookies](https://en.wikipedia.org/wiki/HTTP_cookie "HTTP cookie"). For this to work, every time the user downloads a page, a unique identifier must be chosen and added as a query string to the URLs of all links the page contains. As soon as the user follows one of these links, the corresponding URL is requested to the server. This way, the download of this page is linked with the previous one.

For example, when a web page containing the following is requested:

 <a href="foo.html">see my page!</a>
  <a href="bar.html">mine is better</a>

a unique string, such as  `e0a72cb2a2c7`  is chosen, and the page is modified as follows:

 <a href="foo.html?e0a72cb2a2c7">see my page!</a>
  <a href="bar.html?e0a72cb2a2c7">mine is better</a>

The addition of the query string does not change the way the page is shown to the user. When the user follows, for example, the first link, the browser requests the page  `foo.html?e0a72cb2a2c7`  to the server, which ignores what follows  `?`  and sends the page  `foo.html`  as expected, adding the query string to its links as well.

This way, any subsequent page request from this user will carry the same query string  `e0a72cb2a2c7`, making it possible to establish that all these pages have been viewed by the same user. Query strings are often used in association with  [web beacons](https://en.wikipedia.org/wiki/Web_beacon "Web beacon").

The main differences between query strings used for tracking and HTTP cookies are that:

1.  Query strings form part of the URL, and are therefore included if the user saves or sends the URL to another user; cookies can be maintained across browsing sessions, but are not saved or sent with the URL.
2.  If the user arrives at the same web server by two (or more) independent paths, it will be assigned two different query strings, while the stored cookies are the same.
3.  The user can disable cookies, in which case using cookies for tracking does not work. However, using query strings for tracking should work in all situations.
4.  Different query strings passed by different visits to the page will mean that the pages are never served from the browser (or proxy, if present) cache thereby increasing the load on the web server and slowing down the user experience.

## Compatibility  issues[[edit](https://en.wikipedia.org/w/index.php?title=Query_string&action=edit&section=7 "Edit section: Compatibility issues")]

According to the  [HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol "Hypertext Transfer Protocol")  specification:

> Various ad hoc limitations on request-line length are found in practice. It is RECOMMENDED that all HTTP senders and recipients support, at a minimum, request-line lengths of 8000 octets.[[14]](https://en.wikipedia.org/wiki/Query_string#cite_note-14)

If the URL is too long, the web server fails with the  [414 Request-URI Too Long](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#414 "List of HTTP status codes")  HTTP status code.

The common workaround for these problems is to use  [POST](https://en.wikipedia.org/wiki/POST_(HTTP) "POST (HTTP)")  instead of  [GET](https://en.wikipedia.org/wiki/GET_(HTTP) "GET (HTTP)")  and store the parameters in the request body. The length limits on request bodies are typically much higher than those on URL length. For example, the limit on POST size, by default, is 2 MB on IIS 4.0 and 128 KB on IIS 5.0. The limit is configurable on Apache2 using the  `LimitRequestBody`  directive, which specifies the number of bytes from 0 (meaning unlimited) to 2147483647 (2 GB) that are allowed in a request body.[[15]](https://en.wikipedia.org/wiki/Query_string#cite_note-15)

## See also[[edit](https://en.wikipedia.org/w/index.php?title=Query_string&action=edit&section=8 "Edit section: See also")]

-   [Clean URL](https://en.wikipedia.org/wiki/Clean_URL "Clean URL")
-   [Click identifier](https://en.wikipedia.org/wiki/DoubleClick_Click_Identifier "DoubleClick Click Identifier")
-   [Common Gateway Interface](https://en.wikipedia.org/wiki/Common_Gateway_Interface "Common Gateway Interface")  (CGI)
-   [HTTP cookie](https://en.wikipedia.org/wiki/HTTP_cookie "HTTP cookie")
-   [HyperText Transfer Protocol](https://en.wikipedia.org/wiki/HyperText_Transfer_Protocol "HyperText Transfer Protocol")  (HTTP)
-   [Semantic URLs](https://en.wikipedia.org/wiki/Semantic_URL "Semantic URL")
-   [URI scheme](https://en.wikipedia.org/wiki/URI_scheme "URI scheme")
-   [UTM parameters](https://en.wikipedia.org/wiki/UTM_parameters "UTM parameters")
-   [Web beacon](https://en.wikipedia.org/wiki/Web_beacon "Web beacon")