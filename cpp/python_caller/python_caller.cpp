#include "python_caller.h"
#include <cstdio>
#include <memory>
#include <stdexcept>

using std::string;
using std::vector;

PythonCaller::PythonCaller(const string& script_path) : _script_path(script_path) {}

string PythonCaller::call(const vector<string>& args) {
    string cmd = "python3 " + _script_path;
    for (const auto& arg : args) {
        cmd += " " + arg;
    }

    std::unique_ptr<FILE, decltype(&pclose)> pipe(popen(cmd.c_str(), "r"), pclose);
    if (!pipe) {
        throw std::runtime_error("Failed to execute python script");
    }

    string result;
    char buffer[128];
    while (fgets(buffer, sizeof(buffer), pipe.get()) != nullptr) {
        result += buffer;
    }
    return result;
}
