import unittest
from pathlib import Path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from score_scripts import doc_score

class TestDocScoring(unittest.TestCase):
    def setUp(self):
        # Common test data setup
        self.base_path = "."  # Adjust path as needed
    
    def test_doc_python_pass(self):
        # Test case for test gen scoring in python on a passing case
        #case-488
        test_case = {
            "case_id": "case-488",
            "file_path": "case-488_file-100635352_pritunl_queues_unassign_ip_addr.py",
            "line_range": [
                26,
                49
            ],
            "command_specific_fields": {
                "terminalOutput": "",
                "debugConsoleOutput": "",
                "activeFileDiagnostics": []
            },
            "language": "python",
            "prompt": ""
        }
        
        model_response = '''def task(self):
    """
    Unassigns an IP address from a server's IP pool.
    
    Attempts to remove IP address assignment from the specified server's IP pool. 
    Will retry up to 5 times if the server has a network lock.
    
    Raises:
        ServerNetworkLocked: If server still has network lock after 5 retries.
    """
    svr = server.get_by_id(self.server_id)

    if not svr:
        logger.warning('Tried to run unassign_ip_pool queue ' +
            'but server is no longer available', 'queues',
            server_id=self.server_id,
        )
        return

    for _ in range(5):
        if svr.network_lock:
            time.sleep(2)
            svr.load()
        else:
            break

    if svr.network_lock:
        raise ServerNetworkLocked('Server network is locked', {
            'server_id': svr.id,
            'queue_id': self.id,
            'queue_type': self.type,
        })

    svr.ip_pool.unassign_ip_addr(self.org_id, self.user_id)'''
        
        result = doc_score.score_doc(
            base_path=self.base_path,
            start_line=test_case["line_range"][0],
            language=test_case["language"],
            relative_file_path=test_case["case_id"] + "/" + test_case["file_path"],
            model_output=model_response
        )

        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 1)

    def test_doc_python_fail(self):
        # Test case for test gen scoring in python on a failing case
        #case-649
        test_case = {
            "case_id": "case-649",
            "file_path": "case-649_file-107391234_chrome_content_papermachines_processors_lib_translate.py",
            "line_range": [
                20,
                31
            ],
            "command_specific_fields": {
                "terminalOutput": "",
                "debugConsoleOutput": "",
                "activeFileDiagnostics": []
            },
            "language": "python",
            "prompt": ""
        }
        model_response = '''def setLanguages(self, out_dir, from_lang="Hebrew", lang_to="English"):
    """
    Set source and target languages for translation and load/initialize translation cache.

    Args:
        out_dir (str): Directory path where translation cache file will be stored
        from_lang (str, optional): Source language. Defaults to "Hebrew"
        lang_to (str, optional): Target language. Defaults to "English"
    """
    from_lang = from_lang.upper()
    lang_to = lang_to.upper()
    self.from_lang = getattr(self.language, from_lang, "HEBREW") 
    self.lang_to = getattr(self.language, lang_to, "ENGLISH")
    joint_lang = re.sub(r"\W+", '', from_lang + lang_to, flags=re.UNICODE)
    self.translate_file = os.path.join(out_dir, "translator" + joint_lang + ".cache")
    if os.path.exists(self.translate_file):
        with codecs.open(self.translate_file, 'r', encoding='utf-8') as f:
            self.translations = json.load(f)
    else:
        self.translations = {}'''
        
        result = doc_score.score_doc(
            base_path=self.base_path,
            start_line=test_case["line_range"][0],
            language=test_case["language"],
            relative_file_path=test_case["case_id"] + "/" + test_case["file_path"],
            model_output=model_response
        )

        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 0)

    def test_doc_js_pass(self):
        # Test case for doc scoring in javascript on a passing case
        #case-6650
        test_case = {
            "case_id": "case-6650",
            "file_path": "case-6650_file-100385759_src_lib_engine_me_index.js",
            "line_range": [
                2,
                7
            ],
            "command_specific_fields": {
                "terminalOutput": "",
                "debugConsoleOutput": "",
                "activeFileDiagnostics": []
            },
            "language": "javascript",
            "prompt": ""
        }
        
        model_response = '''export function spaces(me, graph) {
  /**
   * Filters guesstimates in a graph by matching user IDs.
   * @param {Object} me - User object containing ID information
   * @param {Object} graph - Graph object containing guesstimate data
   * @returns {Array} Array of guesstimate objects matching the user ID
   */
  id = guesstimateId(me)

  if (id) {

    return graph.guesstimates.filter(g => g.user == id)

  }

}'''
        
        result = doc_score.score_doc(
            base_path=self.base_path,
            start_line=test_case["line_range"][0],
            language=test_case["language"],
            relative_file_path=test_case["case_id"] + "/" + test_case["file_path"],
            model_output=model_response
        )

        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 1)
    
    def test_doc_js_fail(self):
    
        # Test case for doc scoring in javascript on a failing case
        #case-5019
        test_case = {
            "case_id": "case-5019",
            "file_path": "case-5019_file-101739008_primefaces_src_main_type-definitions_specs_components_ClassFieldsIgnoresUnrelatedThisContext_input.js",
            "line_range": [
                4,
                21
            ],
            "command_specific_fields": {
                "terminalOutput": "",
                "debugConsoleOutput": "",
                "activeFileDiagnostics": []
            },
            "language": "javascript",
            "prompt": ""
        }
        
        model_response = '''met1() {
    /**
     * A method containing various JavaScript constructs that manipulate 'this.foo'.
     * Includes a named function 'bar', an immediately invoked function expression (IIFE),
     * a class 'Baz' with method 'met2', and an anonymous class with method 'met3'.
     * Each construct sets this.foo to 9.
     */
    function bar() {

        this.foo = 9;

    }

    (function() {

        this.foo = 9;

    })();

    class Baz {

        met2() {

            this.foo = 9;

        }

    }

    new (class {

        met3() {

            this.foo = 9;

        }

    })();

}'''
        
        result = doc_score.score_doc(
            base_path=self.base_path,
            start_line=test_case["line_range"][0],
            language=test_case["language"],
            relative_file_path=test_case["case_id"] + "/" + test_case["file_path"],
            model_output=model_response
        )

        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 0)
    
    def test_doc_ts_pass(self):
    
        # Test case for doc scoring in typescript on a passing case
        #case-4100
        test_case = {
            "case_id": "case-4100",
            "file_path": "case-4100_file-131163161_src_util_styles.ts",
            "line_range": [
                10,
                24
            ],
            "command_specific_fields": {
                "terminalOutput": "",
                "debugConsoleOutput": "",
                "activeFileDiagnostics": []
            },
            "language": "typescript",
            "prompt": ""
        }
        
        model_response = '''function findSelectorMatch(selector: string, regex: RegExp): [string, number] {
    /**
     * Finds matches for a regex pattern in a CSS selector string
     * @param selector CSS selector string to search
     * @param regex Regular expression pattern to match
     * @returns Tuple containing [modified selector with matches replaced by space, number of matches found]
     */
    const matches = regex.exec(selector);

    if (!matches) {
        return [
            selector,
            0
        ];
    }

    return [
        selector.replace(regex, ' '),
        matches.length
    ];
}'''
        
        result = doc_score.score_doc(
            base_path=self.base_path,
            start_line=test_case["line_range"][0],
            language=test_case["language"],
            relative_file_path=test_case["case_id"] + "/" + test_case["file_path"],
            model_output=model_response
        )

        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 1)
    
    def test_doc_ts_fail(self):
    
        # Test case for doc scoring in typescript on a failing case
        #case-5213
        test_case = {
            "case_id": "case-5213",
            "file_path": "case-5213_file-1505889166391_schedule-frontend_src_app_editor_services_drag-and-drop.service.ts",
            "line_range": [
                13,
                21
            ],
            "command_specific_fields": {
                "terminalOutput": "",
                "debugConsoleOutput": "",
                "activeFileDiagnostics": []
            },
            "language": "typescript",
            "prompt": ""
        }
        
        model_response = '''/**
 * Initiates dragging of a class object within the view
 * @param c - The class object being dragged
 * @param viewObjectId - ID of the view object being dragged
 * @param position - Position where the drag started
 */
startDrag(c: Class, viewObjectId: number, position: number): void {

    const classFrequency = frequencyFromString(c.frequency);

    this.dragClass = c;

    this.dragCell = {

        viewObjectId: viewObjectId,

        position: position,

        frequency: classFrequency

    };

}'''
        
        result = doc_score.score_doc(
            base_path=self.base_path,
            start_line=test_case["line_range"][0],
            language=test_case["language"],
            relative_file_path=test_case["case_id"] + "/" + test_case["file_path"],
            model_output=model_response
        )

        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 0)

#TODO: Add more test cases for cpp/java/csharp once fully implemented

if __name__ == '__main__':
    unittest.main() 
    # Usage for running a single test:
    # python -m unittest tests.doc_tests.TestMetricsScoring.(test name e.g. test_doc_python_pass)