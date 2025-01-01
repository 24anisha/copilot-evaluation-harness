import unittest
from pathlib import Path
from score_scripts import test_score, fix_score, doc_score, model_handler
from end_to_end_script import create_model_input
import os
from absl import flags
import sys
import anthropic

class TestMetricsScoring(unittest.TestCase):
    def setUp(self):
        # Common test data setup
        self.base_path = "out/repos/test_repo"  # Adjust path as needed
        
    def test_fix_python(self):
        # Test case for fix scoring in python
        test_case = {
            "repo_name": "yt-dlp/yt-dlp",
            "file_path": "yt_dlp/extractor/unsupported.py",
            "language": "python",
            "command_specific_fields": {
                "static_analyzer": "pylint",
                "rule": "pylint-no-self-argument",
                "analyzer_error": 'Method \'IE_NAME\' should have "self" as first argument'
            }
        }
        
        model_response = '''from .common import InfoExtractor
from ..utils import ExtractorError, classproperty, remove_start


class UnsupportedInfoExtractor(InfoExtractor):
    IE_DESC = False
    URLS = ()  # Redefine in subclasses

    @classproperty
    def IE_NAME(cls):
        return remove_start(cls.__name__, 'Known')

    @classproperty
    def _VALID_URL(cls):
        return rf'https?://(?:www\.)?(?:{"|".join(cls.URLS)})'


LF = '
       '


class KnownDRMIE(UnsupportedInfoExtractor):
    """Sites that are known to use DRM for all their videos

    Add to this list only if:
    * You are reasonably certain that the site uses DRM for ALL their videos
    * Multiple users have asked about this site on github/discord
    """

    URLS = (
        r'play\.hbomax\.com',
        r'channel(?:4|5)\.com',
        r'peacocktv\.com',
        r'(?:[\w\.]+\.)?disneyplus\.com',
        r'open\.spotify\.com/(?:track|playlist|album|artist)',
        r'tvnz\.co\.nz',
        r'oneplus\.ch',
        r'artstation\.com/learning/courses',
        r'philo\.com',
        r'(?:[\w\.]+\.)?mech-plus\.com',
        r'aha\.video',
        r'mubi\.com',
        r'vootkids\.com',
        r'nowtv\.it/watch',
        r'tv\.apple\.com',
        r'primevideo\.com',
        r'hulu\.com',
        r'resource\.inkryptvideos\.com',
        r'joyn\.de',
        r'amazon\.(?:\w{2}\.)?\w+/gp/video',
        r'music\.amazon\.(?:\w{2}\.)?\w+',
        r'(?:watch|front)\.njpwworld\.com',
        r'qub\.ca/vrai',
    )

    _TESTS = [{
        # https://github.com/yt-dlp/yt-dlp/issues/4309
        'url': 'https://peacocktv.com/watch/playback/vod/GMO_00000000073159_01/f9d03003-eb04-3c7f-a7b6-a83ab7eb55bc',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/1719,
        'url': 'https://www.channel4.com/programmes/gurren-lagann/on-demand/69960-001',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/1548
        'url': 'https://www.channel5.com/show/uk-s-strongest-man-2021/season-2021/episode-1',
        'only_matching': True,
    }, {
        'url': r'https://hsesn.apps.disneyplus.com',
        'only_matching': True,
    }, {
        'url': r'https://www.disneyplus.com',
        'only_matching': True,
    }, {
        'url': 'https://open.spotify.com/artist/',
        'only_matching': True,
    }, {
        'url': 'https://open.spotify.com/track/',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/4122
        'url': 'https://www.tvnz.co.nz/shows/ice-airport-alaska/episodes/s1-e1',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/1922
        'url': 'https://www.oneplus.ch/play/1008188',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/1140
        'url': 'https://www.artstation.com/learning/courses/dqQ/character-design-masterclass-with-serge-birault/chapters/Rxn3/introduction',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/3544
        'url': 'https://www.philo.com/player/player/vod/Vk9EOjYwODU0ODg5OTY0ODY0OTQ5NA',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/3533
        'url': 'https://www.mech-plus.com/player/24892/stream?assetType=episodes&playlist_id=6',
        'only_matching': True,
    }, {
        'url': 'https://watch.mech-plus.com/details/25240?playlist_id=6',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/2934
        'url': 'https://www.aha.video/player/movie/lucky-man',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/2743
        'url': 'https://mubi.com/films/the-night-doctor',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/3287
        'url': 'https://www.vootkids.com/movies/chhota-bheem-the-rise-of-kirmada/764459',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/2744
        'url': 'https://www.nowtv.it/watch/home/asset/and-just-like-that/skyserie_f8fe979772e8437d8a61ab83b6d293e9/seasons/1/episodes/8/R_126182_HD',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/5557
        'url': 'https://tv.apple.com/it/show/loot---una-fortuna/umc.cmc.5erbujil1mpazuerhr1udnk45?ctx_brand=tvs.sbd.4000',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/3072
        'url': 'https://www.joyn.de/play/serien/clannad/1-1-wo-die-kirschblueten-fallen',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/7323
        'url': 'https://music.amazon.co.jp/albums/B088Y368TK',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/7323
        'url': 'https://www.amazon.co.jp/gp/video/detail/B09X5HBYRS/',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/6125
        'url': 'https://www.primevideo.com/region/eu/detail/0H3DDB4KBJFNDCKKLHNRLRLVKQ/ref=atv_br_def_r_br_c_unkc_1_10',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/5740
        'url': 'https://resource.inkryptvideos.com/v2-a83ns52/iframe/index.html#video_id=7999ea0f6e03439eb40d056258c2d736&otp=xxx',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/5767
        'url': 'https://www.hulu.com/movie/anthem-6b25fac9-da2b-45a3-8e09-e4156b0471cc',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/pull/8570
        'url': 'https://watch.njpwworld.com/player/36447/series?assetType=series',
        'only_matching': True,
    }, {
        'url': 'https://front.njpwworld.com/p/s_series_00563_16_bs',
        'only_matching': True,
    }, {
        'url': 'https://www.qub.ca/vrai/l-effet-bocuse-d-or/saison-1/l-effet-bocuse-d-or-saison-1-bande-annonce-1098225063',
        'only_matching': True,
    }]

    def _real_extract(self, url):
        raise ExtractorError(
            f'The requested site is known to use DRM protection. '
            f'It will {self._downloader._format_err("NOT", self._downloader.Styles.EMPHASIS)} be supported.{LF}'
            f'Please {self._downloader._format_err("DO NOT", self._downloader.Styles.ERROR)} open an issue, '
            'unless you have evidence that the video is not DRM protected', expected=True)


class KnownPiracyIE(UnsupportedInfoExtractor):
    """Sites that have been deemed to be piracy

    In order for this to not end up being a catalog of piracy sites,
    only sites that were once supported should be added to this list
    """

    URLS = (
        r'dood\.(?:to|watch|so|pm|wf|re)',
        # Sites youtube-dl supports, but we won't
        r'viewsb\.com',
        r'filemoon\.sx',
        r'hentai\.animestigma\.com',
        r'thisav\.com',
        r'gounlimited\.to',
        r'highstream\.tv',
        r'uqload\.com',
        r'vedbam\.xyz',
        r'vadbam\.net'
        r'vidlo\.us',
        r'wolfstream\.tv',
        r'xvideosharing\.com',
        r'(?:\w+\.)?viidshar\.com',
        r'sxyprn\.com',
        r'jable\.tv',
        r'91porn\.com',
        r'einthusan\.(?:tv|com|ca)',
        r'yourupload\.com',
    )

    _TESTS = [{
        'url': 'http://dood.to/e/5s1wmbdacezb',
        'only_matching': True,
    }, {
        'url': 'https://thisav.com/en/terms',
        'only_matching': True,
    }]

    def _real_extract(self, url):
        raise ExtractorError(
            f'This website is no longer supported since it has been determined to be primarily used for piracy.{LF}'
            f'{self._downloader._format_err("DO NOT", self._downloader.Styles.ERROR)} open issues for it', expected=True)
'''
        
        result = fix_score.score_fix(
            base_path=f"{self.base_path}",
            repo_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            task=test_case["command_specific_fields"]["static_analyzer"],
            language=test_case["language"],
            model_response=model_response
        )
        print("\nFix Python Result:", result)
        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)
    

    def test_fix_js(self):
        # Test case for fix scoring in javascript
        test_case = {
            "repo_name": "jmreidy/grunt-browserify",
            "file_path": "examples/watch/public/main.js",
            "language": "javascript",
            "command_specific_fields": {
                "static_analyzer": "eslint",
                "rule": "eslint-no-unreachable-loop",
                "analyzer_error": "Invalid loop. Its body allows only one interaction."
            }
        }
        # TODO: get a sample model response for javascript
        model_response = """

"""
        
        result = fix_score.score_fix(
            base_path=f"{self.base_path}",
            repo_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            task=test_case["command_specific_fields"]["static_analyzer"],
            language=test_case["language"],
            model_response=model_response
        )
        print("\nFix JS Result:", result)
        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

    def test_test_gen_python(self):
        # Test case for test gen scoring in python
        test_case = {
            "repo_name": "google/yapf",
            "file_path": "yapf/pytree/subtype_assigner.py",
            "language": "python"
        }
        
        model_response = """
def test_visit_node_with_caret_leaf():
  node = pytree.Node(None, [
    pytree.Leaf(None, '^'),
    pytree.Leaf(None, 'x')
  ])
  visitor = StyleVisitor()
  visitor.Visit(node)
  assert node.children[0].subtypes == [subtypes.BINARY_OPERATOR]
"""
        
        result = test_score.score_test(
            base_path=f"{self.base_path}",
            repo_folder_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            language=test_case["language"],
            model_response=model_response
        )
        print("\nTest Gen Python Result:", result)
        
        self.assertIsInstance(result, dict)
        if not result.get('success', False):
            self.fail(f"Test generation failed: {result.get('reason', 'No reason provided')}")

    def test_test_gen_js(self):
        # Test case for test gen scoring in javascript
        test_case = {
            "repo_name": "rastapasta/mapscii",
            "file_path": "src/Mapscii.js",
            "language": "javascript"
        }
        
        model_response = """
describe('Renderer Tests', () => {
  let component;
  let mockRenderer;

  beforeEach(() => {
    mockRenderer = {
      draw: jest.fn()
    };
    component = {
      renderer: mockRenderer,
      center: [0, 0],
      zoom: 1,
      _write: jest.fn(),
      notify: jest.fn(),
      _getFooter: jest.fn()
    };
  });

  it('should handle successful render', async () => {
    const frame = 'test frame';
    const footer = 'test footer';
    mockRenderer.draw.mockResolvedValue(frame);
    component._getFooter.mockReturnValue(footer);

    await component.renderer.draw(component.center, component.zoom);

    expect(mockRenderer.draw).toHaveBeenCalledWith(component.center, component.zoom);
    expect(component._write).toHaveBeenCalledWith(frame);
    expect(component.notify).toHaveBeenCalledWith(footer);
  });

  it('should handle renderer busy error', async () => {
    mockRenderer.draw.mockRejectedValue(new Error());

    await component.renderer.draw(component.center, component.zoom);

    expect(mockRenderer.draw).toHaveBeenCalledWith(component.center, component.zoom);
    expect(component.notify).toHaveBeenCalledWith('renderer is busy');
  });
});
"""
        
        result = test_score.score_test(
            base_path=f"{self.base_path}",
            repo_folder_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            language=test_case["language"],
            model_response=model_response
        )
        print("\nTest Gen JS Result:", result)
        
        self.assertIsInstance(result, dict)
        if not result.get('success', False):
            self.fail(f"Test generation failed: {result.get('reason', 'No reason provided')}")

    def test_doc_python(self):
        # Test case for doc scoring in python
        # TODO: duplicate this for javascript
        test_case = {
            "case_id": "case-101",
            "file_path": "case-101_file-111823297_peframe_modules_yara_check.py",
            "language": "python",
            "line_range": [7, 18]
        }
        
        model_response = """
Performs YARA rule matching on a target file using rules from a YARA rule file.

Args:
    fileyara (str): Path to the YARA rule file containing pattern definitions
    filename (str): Path to the target file to scan for matches

Returns:
    list: A list of strings representing the matched YARA rules. Returns an empty list if no matches
          are found or if an error occurs during matching.

Notes:
    - Silently handles YARA internal errors by returning an empty list
    - Each match is converted to a string representation before being added to the results
        """
        
        result = doc_score.score_doc(
            base_path=self.base_path,
            start_line=test_case["line_range"][0],
            language=test_case["language"],
            relative_file_path=f"{test_case['case_id']}/{test_case['file_path']}",
            model_output=model_response
        )
        print("\nProcess Doc Result:", result)
        
        self.assertIsInstance(result, dict)
        if not result.get('success', False):
            self.fail(f"Docstring generation failed: {result.get('reason', 'No reason provided')}")
    
    # For model inputs, tests are currently written to check that the prompt is passed in correctly and that the code is not empty.
    # TODO: Check that code being passed in is correct (e.g. whole file for fix, function for test_gen, etc.)

    def test_model_input_fix(self):
        # no optional prompt passed
        if not flags.FLAGS.is_parsed():
            flags.FLAGS(["test_metrics.py", "--metric=fix"])
        test_case = {
            "repo_name": "yt-dlp/yt-dlp",
            "file_path": "yt_dlp/extractor/unsupported.py",
            "language": "python",
            "command_specific_fields": {
                "static_analyzer": "pylint",
                "rule": "pylint-no-self-argument",
                "analyzer_error": 'Method \'IE_NAME\' should have "self" as first argument'
            },
            "code_snippet": "code here" # TODO: update
        }
        data_dir = os.path.join('data', 'fix')

        model_input = create_model_input(test_case, self.base_path)
        print("\nFix Model Input:", model_input)

        self.assertNotEqual(model_input.splitlines()[1], "</prompt>") # checks that prompt is not empty
        self.assertNotEqual(model_input.splitlines()[-2], "<code>") # checks that code is not empty

        self.assertEqual(model_input.splitlines()[1], "Fix the error in the following code. Provide only the fixed code, with no excess text.") #checks that prompt is correct
    
    def test_model_input_test_gen(self):
        # no optional prompt passed
        if not flags.FLAGS.is_parsed():
            flags.FLAGS(["test_metrics.py", "--metric=test_gen"])
        test_case = {
            "repo_name": "google/yapf",
            "file_path": "yapf/pytree/subtype_assigner.py",
            "language": "python",
            "code_snippet": "code here" # TODO: update
        }

        model_input = create_model_input(test_case, self.base_path)
        print("\nTest Gen Model Input:", model_input)

        self.assertNotEqual(model_input.splitlines()[1], "</prompt>") # checks that prompt is not empty
        self.assertNotEqual(model_input.splitlines()[-2], "<code>") # checks that code is not empty
        
        self.assertEqual(model_input.splitlines()[1], "Write a unit test for the following. Only provide the unit test, with no excess text.") #checks that prompt is correct
    
    def test_model_input_doc(self):
        # no optional prompt passed
        if not flags.FLAGS.is_parsed():
            flags.FLAGS(["test_metrics.py", "--metric=doc"])
        test_case = {
            "case_id": "case-101",
            "file_path": "case-101_file-111823297_peframe_modules_yara_check.py",
            "language": "python",
            "line_range": [7, 18]
        }

        model_input = create_model_input(test_case, self.base_path)
        print("\nDoc Model Input:", model_input)

        self.assertNotEqual(model_input.splitlines()[1], "</prompt>") # checks that prompt is not empty
        self.assertNotEqual(model_input.splitlines()[-2], "<code>") # checks that code is not empty
        
        self.assertEqual(model_input.splitlines()[1], "Write a docstring for the following function. Only provide the docstring, with no excess text.") #checks that prompt is correct

    # For model response status, only have test for anthropic as it is only available model.
    def test_anthropic_response(self):
        api_key = os.getenv("API_KEY")
        if not api_key:
            print("Error: The environment variable 'API_KEY' is not set.")
            sys.exit(1)

        try:
            model = anthropic.Anthropic(api_key=api_key)
            response = model.messages.create(
                model='claude-3-5-sonnet-20241022',
                max_tokens=8000,
                messages=[
                    {"role": "user", "content": "Hello, world!"}
                ]
            )
            # The response object doesn't directly expose HTTP status codes
            # A successful response means the request went through (equivalent to 200)
            print("Request successful!")
            print("Response content:", response.content)
            self.assertTrue(True)
        
        except anthropic.AnthropicError as e:
            print(f"API Error: {str(e)}")
            self.assertTrue(False)
            
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.assertTrue(False)
            
    def test_fix_model_gen(self):
        # Test case to check whether model yields a properly formatted output for fix metric
        if not flags.FLAGS.is_parsed():
            flags.FLAGS(["test_metrics.py", "--metric=fix"])
        test_case = {
            "repo_name": "yt-dlp/yt-dlp",
            "file_path": "yt_dlp/extractor/unsupported.py",
            "language": "python",
            "command_specific_fields": {
                "static_analyzer": "pylint",
                "rule": "pylint-no-self-argument",
                "analyzer_error": 'Method \'IE_NAME\' should have "self" as first argument'
            },
            "code_snippet": '''from .common import InfoExtractor
from ..utils import ExtractorError, classproperty, remove_start


class UnsupportedInfoExtractor(InfoExtractor):
    IE_DESC = False
    URLS = ()  # Redefine in subclasses

    @classproperty
    def IE_NAME(cls):
        return remove_start(super().IE_NAME, 'Known')

    @classproperty
    def _VALID_URL(cls):
        return rf'https?://(?:www\.)?(?:{"|".join(cls.URLS)})'


LF = '\n       '


class KnownDRMIE(UnsupportedInfoExtractor):
    """Sites that are known to use DRM for all their videos

    Add to this list only if:
    * You are reasonably certain that the site uses DRM for ALL their videos
    * Multiple users have asked about this site on github/discord
    """

    URLS = (
        r'play\.hbomax\.com',
        r'channel(?:4|5)\.com',
        r'peacocktv\.com',
        r'(?:[\w\.]+\.)?disneyplus\.com',
        r'open\.spotify\.com/(?:track|playlist|album|artist)',
        r'tvnz\.co\.nz',
        r'oneplus\.ch',
        r'artstation\.com/learning/courses',
        r'philo\.com',
        r'(?:[\w\.]+\.)?mech-plus\.com',
        r'aha\.video',
        r'mubi\.com',
        r'vootkids\.com',
        r'nowtv\.it/watch',
        r'tv\.apple\.com',
        r'primevideo\.com',
        r'hulu\.com',
        r'resource\.inkryptvideos\.com',
        r'joyn\.de',
        r'amazon\.(?:\w{2}\.)?\w+/gp/video',
        r'music\.amazon\.(?:\w{2}\.)?\w+',
        r'(?:watch|front)\.njpwworld\.com',
        r'qub\.ca/vrai',
    )

    _TESTS = [{
        # https://github.com/yt-dlp/yt-dlp/issues/4309
        'url': 'https://peacocktv.com/watch/playback/vod/GMO_00000000073159_01/f9d03003-eb04-3c7f-a7b6-a83ab7eb55bc',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/1719,
        'url': 'https://www.channel4.com/programmes/gurren-lagann/on-demand/69960-001',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/1548
        'url': 'https://www.channel5.com/show/uk-s-strongest-man-2021/season-2021/episode-1',
        'only_matching': True,
    }, {
        'url': r'https://hsesn.apps.disneyplus.com',
        'only_matching': True,
    }, {
        'url': r'https://www.disneyplus.com',
        'only_matching': True,
    }, {
        'url': 'https://open.spotify.com/artist/',
        'only_matching': True,
    }, {
        'url': 'https://open.spotify.com/track/',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/4122
        'url': 'https://www.tvnz.co.nz/shows/ice-airport-alaska/episodes/s1-e1',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/1922
        'url': 'https://www.oneplus.ch/play/1008188',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/1140
        'url': 'https://www.artstation.com/learning/courses/dqQ/character-design-masterclass-with-serge-birault/chapters/Rxn3/introduction',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/3544
        'url': 'https://www.philo.com/player/player/vod/Vk9EOjYwODU0ODg5OTY0ODY0OTQ5NA',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/3533
        'url': 'https://www.mech-plus.com/player/24892/stream?assetType=episodes&playlist_id=6',
        'only_matching': True,
    }, {
        'url': 'https://watch.mech-plus.com/details/25240?playlist_id=6',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/2934
        'url': 'https://www.aha.video/player/movie/lucky-man',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/2743
        'url': 'https://mubi.com/films/the-night-doctor',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/3287
        'url': 'https://www.vootkids.com/movies/chhota-bheem-the-rise-of-kirmada/764459',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/2744
        'url': 'https://www.nowtv.it/watch/home/asset/and-just-like-that/skyserie_f8fe979772e8437d8a61ab83b6d293e9/seasons/1/episodes/8/R_126182_HD',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/5557
        'url': 'https://tv.apple.com/it/show/loot---una-fortuna/umc.cmc.5erbujil1mpazuerhr1udnk45?ctx_brand=tvs.sbd.4000',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/3072
        'url': 'https://www.joyn.de/play/serien/clannad/1-1-wo-die-kirschblueten-fallen',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/7323
        'url': 'https://music.amazon.co.jp/albums/B088Y368TK',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/7323
        'url': 'https://www.amazon.co.jp/gp/video/detail/B09X5HBYRS/',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/6125
        'url': 'https://www.primevideo.com/region/eu/detail/0H3DDB4KBJFNDCKKLHNRLRLVKQ/ref=atv_br_def_r_br_c_unkc_1_10',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/5740
        'url': 'https://resource.inkryptvideos.com/v2-a83ns52/iframe/index.html#video_id=7999ea0f6e03439eb40d056258c2d736&otp=xxx',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/issues/5767
        'url': 'https://www.hulu.com/movie/anthem-6b25fac9-da2b-45a3-8e09-e4156b0471cc',
        'only_matching': True,
    }, {
        # https://github.com/yt-dlp/yt-dlp/pull/8570
        'url': 'https://watch.njpwworld.com/player/36447/series?assetType=series',
        'only_matching': True,
    }, {
        'url': 'https://front.njpwworld.com/p/s_series_00563_16_bs',
        'only_matching': True,
    }, {
        'url': 'https://www.qub.ca/vrai/l-effet-bocuse-d-or/saison-1/l-effet-bocuse-d-or-saison-1-bande-annonce-1098225063',
        'only_matching': True,
    }]

    def _real_extract(self, url):
        raise ExtractorError(
            f'The requested site is known to use DRM protection. '
            f'It will {self._downloader._format_err("NOT", self._downloader.Styles.EMPHASIS)} be supported.{LF}'
            f'Please {self._downloader._format_err("DO NOT", self._downloader.Styles.ERROR)} open an issue, '
            'unless you have evidence that the video is not DRM protected', expected=True)


class KnownPiracyIE(UnsupportedInfoExtractor):
    """Sites that have been deemed to be piracy

    In order for this to not end up being a catalog of piracy sites,
    only sites that were once supported should be added to this list
    """

    URLS = (
        r'dood\.(?:to|watch|so|pm|wf|re)',
        # Sites youtube-dl supports, but we won't
        r'viewsb\.com',
        r'filemoon\.sx',
        r'hentai\.animestigma\.com',
        r'thisav\.com',
        r'gounlimited\.to',
        r'highstream\.tv',
        r'uqload\.com',
        r'vedbam\.xyz',
        r'vadbam\.net'
        r'vidlo\.us',
        r'wolfstream\.tv',
        r'xvideosharing\.com',
        r'(?:\w+\.)?viidshar\.com',
        r'sxyprn\.com',
        r'jable\.tv',
        r'91porn\.com',
        r'einthusan\.(?:tv|com|ca)',
        r'yourupload\.com',
    )

    _TESTS = [{
        'url': 'http://dood.to/e/5s1wmbdacezb',
        'only_matching': True,
    }, {
        'url': 'https://thisav.com/en/terms',
        'only_matching': True,
    }]

    def _real_extract(self, url):
        raise ExtractorError(
            f'This website is no longer supported since it has been determined to be primarily used for piracy.{LF}'
            f'{self._downloader._format_err("DO NOT", self._downloader.Styles.ERROR)} open issues for it', expected=True)
'''
        }
        data_dir = os.path.join('data', 'fix')

        model_input = create_model_input(test_case, self.base_path)
        print("\nFix Model Input:", model_input)

        api_key = os.getenv("API_KEY")
        if not api_key:
            print("Error: The environment variable 'API_KEY' is not set.")
            self.fail("API_KEY not set")

        model = model_handler.ModelHandler(model_endpoint="anthropic", model_name="claude-3-sonnet-20240229", token_count=4096)
        model_response = model.call_model(model_input)
        print("\nModel Response:", model_response)

        # Add assertions to verify model response
        self.assertIsNotNone(model_response)
        self.assertIsInstance(model_response, str)
        self.assertNotEqual(model_response.strip(), "")

        # Format validation checks
        self.assertIn("---FIND:", model_response, 
            "Response missing '---FIND:' section")
        self.assertIn("---REPLACE:", model_response, 
            "Response missing '---REPLACE:' section")
        
        # Split response into sections
        try:
            find_section = model_response.split("---FIND:")[1].split("---REPLACE:")[0].strip()
            replace_section = model_response.split("---REPLACE:")[1].strip()
            
            # Verify sections are not empty
            self.assertNotEqual(find_section, "", 
                "FIND section is empty")
            self.assertNotEqual(replace_section, "", 
                "REPLACE section is empty")
            
            # Verify no extra text outside sections
            response_parts = model_response.split("---FIND:")
            if len(response_parts) > 1:
                pre_text = response_parts[0].strip()
                self.assertEqual(pre_text, "", 
                    f"Found extra text before FIND section: '{pre_text}'")
                
            post_text = model_response.split("---REPLACE:")[1].split("\n")
            if len(post_text) > 1:
                last_line = post_text[-1].strip()
                # If last line is not whitespace or does not have closing characters, assume there is extraneous text
                if last_line and not any(c in last_line for c in ['}', ')', ']']):
                    self.fail(f"Found extra text after REPLACE section: '{last_line}'")
                    
        except IndexError:
            self.fail("Response does not follow the required format")
            

if __name__ == '__main__':
    unittest.main() 
    # Usage for running a single test:
    # python -m unittest test_metrics.TestMetricsScoring.(test name e.g. test_fix_python)