#ifndef PYTHON_CALLER_H
#define PYTHON_CALLER_H

#include <string>
#include <vector>
#include <string>

class PythonCaller {
public:
    explicit PythonCaller(const std::string& script_path);

    std::string call(const std::vector<std::string>& args);

private:
    std::string _script_path;
};

#endif
