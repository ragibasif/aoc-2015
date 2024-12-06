import System.IO ()

processFile :: String -> IO ()
processFile contents = do
  putStrLn $ "File contents:\n" ++ contents

main :: IO ()
main = do
  contents <- readFile "input.txt"
  processFile contents

