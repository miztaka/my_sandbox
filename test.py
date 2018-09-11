## サンドボックス環境
sandbox = {}

## builtin関数を必要なものだけsandboxにセット
for f in dir(builtins):
  if f in removeFuncList:
    continue
  else:
    sandbox[f] = getattr(builtins, f)

## import関数を置き換え
sandbox['__import__'] = myImport

## builtin ネームスペース置き換え
namespace = {
  "__builtins__": sandbox
}

## ソースコンパイル & exec
code = compile(algo_src, sourcePath, "exec")
exec(code, namespace)
