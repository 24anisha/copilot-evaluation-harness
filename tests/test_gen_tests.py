import unittest
from pathlib import Path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from score_scripts import test_score
from end_to_end_script import create_model_input
from absl import flags
import anthropic

class TestTestGenScoring(unittest.TestCase):
    def setUp(self):
        # Common test data setup
        self.base_path = "out/repos/test_repo"  # Adjust path as needed

    def test_test_gen_python_pass(self):
        # Test case for test gen scoring in python
        #case-1663
        test_case = {
            "case_id": "case-1663",
            "repo_name": "trekhleb/learn-python",
            "file_path": "src/modules/sound_package/formats/wav.py",
            "code_snippet": "\n\ndef wav_read():\n\n    \"\"\"WAV file reading function mock\"\"\"\n\n    return 'Read from WAV file'\n",
            "line_range": [
                2,
                6
            ],
            "command_specific_fields": {
                "method_name": "wav_read"
            },
            "language": "python",
            "commit": "52c3a655cc2efd5ac01004f6f529c3262812a84e",
            "prompt": ""
        }
        
        model_response = """import unittest
from src.modules.sound_package.formats.wav import wav_read

class TestWavRead(unittest.TestCase):
    def test_wav_read_returns_string(self):
        result = wav_read()
        self.assertEqual(result, 'Read from WAV file')
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()"""
        
        result = test_score.score_test(
            base_path=os.path.join("./out/repos", test_case["repo_name"]),
            repo_folder_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            language=test_case["language"],
            model_response=model_response,
            case_id=test_case["case_id"],
            commit_sha=test_case["commit"],
            test=True
        )

        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 1)
    
    def test_test_gen_python_fail(self):
        # Test case for test gen scoring in python
        #case-1679
        test_case = {
            "case_id": "case-1679",
            "repo_name": "lra/mackup",
            "file_path": "mackup/utils.py",
            "code_snippet": "\n\ndef is_process_running(process_name):\n\n    \"\"\"\n\n    Check if a process with the given name is running.\n\n\n\n    Args:\n\n        (str): Process name, e.g. \"Sublime Text\"\n\n\n\n    Returns:\n\n        (bool): True if the process is running\n\n    \"\"\"\n\n    is_running = False\n\n\n\n    # On systems with pgrep, check if the given process is running\n\n    if os.path.isfile(\"/usr/bin/pgrep\"):\n\n        dev_null = open(os.devnull, \"wb\")\n\n        returncode = subprocess.call([\"/usr/bin/pgrep\", process_name], stdout=dev_null)\n\n        is_running = bool(returncode == 0)\n\n\n\n    return is_running\n",
            "line_range": [
                271,
                291
            ],
            "command_specific_fields": {
                "method_name": "is_process_running"
            },
            "language": "python",
            "commit": "0def08b8543ac3a436257cce4426a5b109b31a2d",
            "prompt": ""
        }
        
        model_response = """import os
import subprocess
from unittest import TestCase
from unittest.mock import patch

class TestIsProcessRunning(TestCase):

    @patch('os.path.isfile')
    @patch('subprocess.call')
    def test_process_running(self, mock_call, mock_isfile):
        mock_isfile.return_value = True
        mock_call.return_value = 0
        
        self.assertTrue(is_process_running("test_process"))
        mock_call.assert_called_once()
        mock_isfile.assert_called_once_with("/usr/bin/pgrep")

    @patch('os.path.isfile') 
    @patch('subprocess.call')
    def test_process_not_running(self, mock_call, mock_isfile):
        mock_isfile.return_value = True
        mock_call.return_value = 1
        
        self.assertFalse(is_process_running("test_process"))
        mock_call.assert_called_once()
        mock_isfile.assert_called_once_with("/usr/bin/pgrep")

    @patch('os.path.isfile')
    def test_pgrep_not_available(self, mock_isfile):
        mock_isfile.return_value = False
        
        self.assertFalse(is_process_running("test_process"))
        mock_isfile.assert_called_once_with("/usr/bin/pgrep")"""
        
        result = test_score.score_test(
            base_path=os.path.join("./out/repos", test_case["repo_name"]),
            repo_folder_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            language=test_case["language"],
            model_response=model_response,
            case_id=test_case["case_id"],
            commit_sha=test_case["commit"],
            test=True
        )

        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 0)

    def test_test_gen_js_pass(self):
        # Test case for test gen scoring in python
        #case-377
        test_case = {
            "case_id": "case-377",
            "repo_name": "purifycss/purifycss",
            "file_path": "lib/purifycss.js",
            "code_snippet": "\n\nfunction _onceWrap(target, type, listener) {\n\n  var fired = false;\n\n  function g() {\n\n    target.removeListener(type, g);\n\n    if (!fired) {\n\n      fired = true;\n\n      listener.apply(target, arguments);\n\n    }\n\n  }\n\n  g.listener = listener;\n\n  return g;\n\n}\n",
            "line_range": [
                271,
                284
            ],
            "command_specific_fields": {
                "method_name": "_onceWrap"
            },
            "language": "javascript",
            "commit": "be52c1c6b1b6e287b6989428c57f05a79aa135dc",
            "prompt": ""
        }
        
        model_response = """describe('_onceWrap', () => {
  it('should wrap listener to only fire once', () => {
    const target = {
      removeListener: jest.fn()
    };
    
    const listener = jest.fn();
    const type = 'test-event';
    
    const wrapped = _onceWrap(target, type, listener);
    
    // First call should trigger listener
    wrapped('arg1', 'arg2');
    expect(target.removeListener).toHaveBeenCalledWith(type, wrapped);
    expect(listener).toHaveBeenCalledWith('arg1', 'arg2');
    expect(listener.mock.calls.length).toBe(1);

    // Second call should not trigger listener again
    wrapped('arg3', 'arg4'); 
    expect(listener.mock.calls.length).toBe(1);
  });

  it('should store original listener reference', () => {
    const target = {
      removeListener: jest.fn()
    };
    const listener = jest.fn();
    const wrapped = _onceWrap(target, 'test', listener);
    
    expect(wrapped.listener).toBe(listener);
  });
});"""
        
        result = test_score.score_test(
            base_path=os.path.join("./out/repos", test_case["repo_name"]),
            repo_folder_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            language=test_case["language"],
            model_response=model_response,
            case_id=test_case["case_id"],
            commit_sha=test_case["commit"],
            test=True
        )

        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 1)

    def test_test_gen_js_fail(self):
        # Test case for test gen scoring in python
        #case-13
        test_case = {
            "case_id": "case-13",
            "repo_name": "tj/commander.js",
            "file_path": "lib/suggestSimilar.js",
            "code_snippet": "\n\nfunction suggestSimilar(word, candidates) {\n\n  if (!candidates || candidates.length === 0) return '';\n\n  // remove possible duplicates\n\n  candidates = Array.from(new Set(candidates));\n\n\n\n  const searchingOptions = word.startsWith('--');\n\n  if (searchingOptions) {\n\n    word = word.slice(2);\n\n    candidates = candidates.map((candidate) => candidate.slice(2));\n\n  }\n\n\n\n  let similar = [];\n\n  let bestDistance = maxDistance;\n\n  const minSimilarity = 0.4;\n\n  candidates.forEach((candidate) => {\n\n    if (candidate.length <= 1) return; // no one character guesses\n\n\n\n    const distance = editDistance(word, candidate);\n\n    const length = Math.max(word.length, candidate.length);\n\n    const similarity = (length - distance) / length;\n\n    if (similarity > minSimilarity) {\n\n      if (distance < bestDistance) {\n\n        // better edit distance, throw away previous worse matches\n\n        bestDistance = distance;\n\n        similar = [candidate];\n\n      } else if (distance === bestDistance) {\n\n        similar.push(candidate);\n\n      }\n\n    }\n\n  });\n\n\n\n  similar.sort((a, b) => a.localeCompare(b));\n\n  if (searchingOptions) {\n\n    similar = similar.map((candidate) => `--${candidate}`);\n\n  }\n\n\n\n  if (similar.length > 1) {\n\n    return `\\n(Did you mean one of ${similar.join(', ')}?)`;\n\n  }\n\n  if (similar.length === 1) {\n\n    return `\\n(Did you mean ${similar[0]}?)`;\n\n  }\n\n  return '';\n\n}\n",
            "line_range": [
                54,
                99
            ],
            "command_specific_fields": {
            "method_name": "suggestSimilar"
            },
            "language": "javascript",
            "commit": "970ecae402b253de691e6a9066fea22f38fe7431",
            "prompt": ""
        }
        
        model_response = """describe('suggestSimilar', () => {
  it('should return empty string for empty candidates array', () => {
    assert.strictEqual(suggestSimilar('test', []), '');
  });

  it('should return empty string for null candidates', () => {
    assert.strictEqual(suggestSimilar('test', null), '');
  });

  it('should suggest single similar word', () => {
    assert.strictEqual(suggestSimilar('tset', ['test']), '\n(Did you mean test?)');
  });

  it('should suggest multiple similar words', () => {
    assert.strictEqual(
      suggestSimilar('tset', ['test', 'tent']),
      '\n(Did you mean one of tent, test?)'
    );
  });

  it('should handle --option format', () => {
    assert.strictEqual(
      suggestSimilar('--tset', ['--test']),
      '\n(Did you mean --test?)'
    );
  });

  it('should remove duplicates from candidates', () => {
    assert.strictEqual(
      suggestSimilar('tset', ['test', 'test']),
      '\n(Did you mean test?)'
    );
  });

  it('should ignore single character candidates', () => {
    assert.strictEqual(suggestSimilar('a', ['b', 'c']), '');
  });

  it('should return empty string when no similar words found', () => {
    assert.strictEqual(suggestSimilar('xyz', ['abc', 'def']), '');
  });
});
    """
        
        result = test_score.score_test(
            base_path=os.path.join("./out/repos", test_case["repo_name"]),
            repo_folder_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            language=test_case["language"],
            model_response=model_response,
            case_id=test_case["case_id"],
            commit_sha=test_case["commit"],
            test=True
        )

        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 0)
    
    def test_test_gen_ts_pass(self):
        # Test case for test_gen scoring in typescript on a passing case
        #case-619
        test_case = {
            "case_id": "case-619",
            "repo_name": "grid-js/gridjs",
            "file_path": "src/pipeline/pipeline.ts",
            "code_snippet": "   */\n\n  clearCache(): void {\n\n    this.cache = new Map<string, object>();\n\n    this.lastProcessorIndexUpdated = -1;\n\n  }\n",
            "line_range": [
                61,
                66
            ],
            "command_specific_fields": {
                "method_name": "clearCache"
            },
            "language": "typescript",
            "commit": "9a6a53eacdc019c01decfdfa8e77cb800922de3d",
            "prompt": ""
        }

        model_response = """
describe('Pipeline', () => {
  describe('clearCache', () => {
    it('should clear the cache and reset lastProcessorIndexUpdated', () => {
      const pipeline = new Pipeline();
      
      // Set up initial state
      pipeline['cache'].set('key1', {value: 1});
      pipeline['cache'].set('key2', {value: 2}); 
      pipeline['lastProcessorIndexUpdated'] = 5;

      // Call clearCache
      pipeline.clearCache();

      // Verify cache is empty
      expect(pipeline['cache'].size).toBe(0);
      
      // Verify lastProcessorIndexUpdated is reset
      expect(pipeline['lastProcessorIndexUpdated']).toBe(-1);
    });
  });
});"""
        
        result = test_score.score_test(
            base_path=os.path.join("./out/repos", test_case["repo_name"]),
            repo_folder_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            language=test_case["language"],
            model_response=model_response,
            case_id=test_case["case_id"],
            commit_sha=test_case["commit"],
            test=True
        )
        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 1)
    
    def test_test_gen_ts_fail(self):
        # Test case for test_gen scoring in typescript on a failing case
        #case-642
        test_case = {
            "case_id": "case-642",
            "repo_name": "peers/peerjs-server",
            "file_path": "src/services/webSocketServer/index.ts",
            "code_snippet": "\n\n\tprivate _onSocketConnection(socket: WebSocket, req: IncomingMessage): void {\n\n\t\t// An unhandled socket error might crash the server. Handle it first.\n\n\t\tsocket.on(\"error\", (error) => {\n\n\t\t\tthis._onSocketError(error);\n\n\t\t});\n\n\n\n\t\t// We are only interested in the query, the base url is therefore not relevant\n\n\t\tconst { searchParams } = new URL(req.url ?? \"\", \"https://peerjs\");\n\n\t\tconst { id, token, key } = Object.fromEntries(searchParams.entries());\n\n\n\n\t\tif (!id || !token || !key) {\n\n\t\t\tthis._sendErrorAndClose(socket, Errors.INVALID_WS_PARAMETERS);\n\n\t\t\treturn;\n\n\t\t}\n\n\n\n\t\tif (key !== this.config.key) {\n\n\t\t\tthis._sendErrorAndClose(socket, Errors.INVALID_KEY);\n\n\t\t\treturn;\n\n\t\t}\n\n\n\n\t\tconst client = this.realm.getClientById(id);\n\n\n\n\t\tif (client) {\n\n\t\t\tif (token !== client.getToken()) {\n\n\t\t\t\t// ID-taken, invalid token\n\n\t\t\t\tsocket.send(\n\n\t\t\t\t\tJSON.stringify({\n\n\t\t\t\t\t\ttype: MessageType.ID_TAKEN,\n\n\t\t\t\t\t\tpayload: { msg: \"ID is taken\" },\n\n\t\t\t\t\t}),\n\n\t\t\t\t);\n\n\n\n\t\t\t\tsocket.close();\n\n\t\t\t\treturn;\n\n\t\t\t}\n\n\n\n\t\t\tthis._configureWS(socket, client);\n\n\t\t\treturn;\n\n\t\t}\n\n\n\n\t\tthis._registerClient({ socket, id, token });\n\n\t}\n",
            "line_range": [
                65,
                108
            ],
            "command_specific_fields": {
                "method_name": "_onSocketConnection"
            },
            "language": "typescript",
            "commit": "aa4cdbac9cc28aac03c5054ef5b45e6fd6a1f5a3",
            "prompt": ""
        }

        model_response = """
describe('_onSocketConnection', () => {
  let mockSocket: WebSocket;
  let mockReq: IncomingMessage;
  let mockRealm: any;
  let webSocketServer: any;

  beforeEach(() => {
    mockSocket = {
      on: jest.fn(),
      send: jest.fn(),
      close: jest.fn()
    } as any;

    mockReq = {
      url: 'https://peerjs?id=test-id&token=test-token&key=test-key'
    } as any;

    mockRealm = {
      getClientById: jest.fn()
    };

    webSocketServer = {
      _onSocketError: jest.fn(),
      _sendErrorAndClose: jest.fn(),
      _configureWS: jest.fn(),
      _registerClient: jest.fn(),
      realm: mockRealm,
      config: {
        key: 'test-key'
      }
    };
  });

  it('should set up error handler on socket', () => {
    webSocketServer._onSocketConnection(mockSocket, mockReq);
    expect(mockSocket.on).toHaveBeenCalledWith('error', expect.any(Function));
  });

  it('should send error if missing query parameters', () => {
    mockReq.url = 'https://peerjs';
    webSocketServer._onSocketConnection(mockSocket, mockReq);
    expect(webSocketServer._sendErrorAndClose).toHaveBeenCalledWith(mockSocket, Errors.INVALID_WS_PARAMETERS);
  });

  it('should send error if invalid key', () => {
    webSocketServer.config.key = 'different-key';
    webSocketServer._onSocketConnection(mockSocket, mockReq);
    expect(webSocketServer._sendErrorAndClose).toHaveBeenCalledWith(mockSocket, Errors.INVALID_KEY);
  });

  it('should send ID_TAKEN if client exists with different token', () => {
    const mockClient = {
      getToken: () => 'different-token'
    };
    mockRealm.getClientById.mockReturnValue(mockClient);

    webSocketServer._onSocketConnection(mockSocket, mockReq);

    expect(mockSocket.send).toHaveBeenCalledWith(
      JSON.stringify({
        type: MessageType.ID_TAKEN,
        payload: { msg: 'ID is taken' }
      })
    );
    expect(mockSocket.close).toHaveBeenCalled();
  });

  it('should configure WS if client exists with matching token', () => {
    const mockClient = {
      getToken: () => 'test-token'
    };
    mockRealm.getClientById.mockReturnValue(mockClient);

    webSocketServer._onSocketConnection(mockSocket, mockReq);

    expect(webSocketServer._configureWS).toHaveBeenCalledWith(mockSocket, mockClient);
  });

  it('should register new client if client does not exist', () => {
    mockRealm.getClientById.mockReturnValue(null);

    webSocketServer._onSocketConnection(mockSocket, mockReq);

    expect(webSocketServer._registerClient).toHaveBeenCalledWith({
      socket: mockSocket,
      id: 'test-id', 
      token: 'test-token'
    });
  });
});"""
        
        result = test_score.score_test(
            base_path=os.path.join("./out/repos", test_case["repo_name"]),
            repo_folder_name=test_case["repo_name"],
            relative_path=Path(test_case["file_path"]),
            language=test_case["language"],
            model_response=model_response,
            case_id=test_case["case_id"],
            commit_sha=test_case["commit"],
            test=True
        )
        
        # Add assertions based on expected result structure
        self.assertIsInstance(result, dict)
        self.assertIn('score', result)

        # Check if the model response is correct
        self.assertEqual(result["score"], 0)

if __name__ == '__main__':
    unittest.main() 
    # Usage for running a single test:
    # python -m unittest test_metrics.TestTestGenScoring.(test name e.g. test_test_gen_python_pass)