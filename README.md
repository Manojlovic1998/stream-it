# stream-it

Python CLI tool for downloading videos.

## MVP 1.0.0

- Features:
  - [ ] Use json file data format to download, name, and save videos into specific directory.
  - [ ] Download the videos from multiple platforms.
  - [ ] Change network MAC address before running the downloads.
  - [ ] Revert to original MAC address once downloads have completed.

## Tool Usage

### Exceptions

This CLI tool is built with the help of _click_ lib. The _click_ library has built in exception handlers which are used to show error messages or/and abort command execution.

## Legal Issues

This software is distributed under the [MIT license](https://raw.github.com/manojlovic1998/stream-it/master/LICENSE).

In particular, please be aware that

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

Translated to human words:

_In case your use of the software forms the basis of copyright infringement, or you use the software for any other illegal purposes, the authors cannot take any responsibility for you._

I only ship the code here, and how you are going to use it is left to your own discretion.

# Technologies

- [Pipenv](https://pipenv.pypa.io/en/latest/)
  - Used for handling the python shell development environment.
- [JSON Crack](https://jsoncrack.com/)
  - Used to preview the [stdin-example.json]("./stdin-example.json") abstract input example for the minimum viable product.
- [Click](https://click.palletsprojects.com/en/8.1.x/#documentation)
  - Used to speed up the development of cli tool interface. It comes with really nice pre-baked solutions.
- [JSON Schema](https://json-schema.org/implementations.html)
  - Used to validate the json input file schema.
