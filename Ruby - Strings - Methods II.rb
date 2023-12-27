def strike(str)
  "<strike>#{str}</strike>"
end

def mask_article(text, words)
  words.each do |word|
    text.gsub!(word, strike(word))
  end
  text
end
