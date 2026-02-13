import Prelude hiding (filter)

{- helper function to work with 3-tuples -}
first :: (a,b,c) -> a
first (x,_,_) =  x

middle :: (a,b,c) -> b
middle (_,x,_) = x

third :: (a,b,c) -> c
third (_,_,x) = x

{- filter returns True if we should include the commit
 - any commits that are:
 - - from a bot
 - - have lines <= 0
 - should return False
 -}
filter :: (String,String,Int) -> Bool
filter (name,msg,lines) | lines <= 0 = False
                        | take 3 name == "bot" = False
                        | otherwise = True

{- transform large commits (more than 20 lines changed) into commmits with 20 lines changes -}
transform :: (String,String,Int) -> (String,String,Int)
transform (name,msg,lines) | lines > 20 = (name,msg,20)
                           | otherwise = (name,msg,lines)

{- analyze a list of commits recursively -}
analyze :: [(String,String,Int)] -> ([(String,String,Int)],Int,Int)
{- base case, if there are no commits return our empty values -}
analyze [] = ([],0,0)
analyze (x:xs) =
  {- analyze the rest of the list -}
  let tail = analyze xs in
    {- check to see if we use this commit or ignore it -}
    if (filter x) then
      {- if we're using this commit, transform it first -}
      let c = transform x in
      {- merged this commit into the rest of the analyzed list -}
      ([c] ++ first tail,1 + middle tail, third c + third tail)
    else
      {- We don't want to include this commit, so just return the rest of the analyzed list -}
      tail
