import fresh_tomatoes
import media

#movie information container below in the following format:
#  movie_name = media.Movie("movie_name", "movie_storyline", "movie_poster", "movie_trailer")

american_sniper = media.Movie("American Sniper",
                              "U.S. Navy SEAL Chris Kyle (Bradley Cooper) takes his sole mission -- protect his comrades -- to heart and becomes one of the most lethal snipers in American history. His pinpoint accuracy not only saves countless lives but also makes him a prime target of insurgents. Despite grave danger and his struggle to be a good husband and father to his family back in the States, Kyle serves four tours of duty in Iraq. However, when he finally returns home, he finds that he cannot leave the war behind.",
                              "http://t2.gstatic.com/images?q=tbn:ANd9GcSCEJMtX2_SB-ZlvYpabgPb6dwI_bVSY-eVap6aSSSfFq5Ldmxa",
                              "https://www.youtube.com/watch?v=99k3u9ay1gs")
dunkirk = media.Movie("Dunkirk",
                      "In May 1940, Germany advanced into France, trapping Allied troops on the beaches of Dunkirk. Under air and ground cover from British and French forces, troops were slowly and methodically evacuated from the beach using every serviceable naval and civilian vessel that could be found. At the end of this heroic mission, 330,000 French, British, Belgian and Dutch soldiers were safely evacuated.",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcSi8VmNoMYm77iHAsAdsZhABzm_idRwgsU-r3njA4F6HY3-xceC",
                      "https://www.youtube.com/watch?v=T7O7BtBnsG4")
happy_gilmore = media.Movie("Happy Gilmore",
                            "All Happy Gilmore (Adam Sandler) has ever wanted is to be a professional hockey player. But he soon discovers he may actually have a talent for playing an entirely different sport: golf. When his grandmother (Frances Bay) learns she is about to lose her home, Happy joins a golf tournament to try and win enough money to buy it for her. With his powerful driving skills and foulmouthed attitude, Happy becomes an unlikely golf hero -- much to the chagrin of the well-mannered golf professionals.",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcSnneu4p89acvEbINL-XBA1caLXkzCVwvtXej1vqaiyBBsHnuh0",
                            "https://www.youtube.com/watch?v=y1emDAYCfVQ")
split = media.Movie("Split",
                    "Though Kevin (James McAvoy) has evidenced 23 personalities to his trusted psychiatrist, Dr. Fletcher (Betty Buckley), there remains one still submerged who is set to materialize and dominate all of the others. Compelled to abduct three teenage girls led by the willful, observant Casey, Kevin reaches a war for survival among all of those contained within him -- as well as everyone around him -- as the walls between his compartments shatter.",
                    "http://t0.gstatic.com/images?q=tbn:ANd9GcQxZKPueKzPFNEc1Un4x2TecYop4yrTVArVtfgrNzktMqbfehfv",
                    "https://www.youtube.com/watch?v=84TouqfIsiI")
ladder_49 = media.Movie("Ladder 49",
                        "After saving the life of one of the civilians inside, firefighter Jack Morrison (Joaquin Phoenix) finds himself trapped in a burning warehouse with a broken leg. As his friend and mentor, Deputy Chief Mike Kennedy (John Travolta), tries to negotiate a rescue from without, Jack flashes back to various events in his life: the first, awkward days on the force, meeting the woman (Jacinda Barrett) who would become his wife and saving a small girl from a burning building.",
                        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9eaqqDBeSL7SVHBA9gz8WSfSnWxwyKCfTOeoAn2Hk8seiB4mr",
                        "https://www.youtube.com/watch?v=jpU7gzT6CdM")
lone_survivor = media.Movie("Lone Survivor",
                            "In 2005 Afghanistan, Navy SEALs Marcus Luttrell (Mark Wahlberg), Michael Murphy (Taylor Kitsch), Danny Dietz (Emile Hirsch) and Matthew "Axe" Axelson (Ben Foster) deploy on a mission of surveillance and to take out Taliban leader Ahmad Shah. Though spotted by goatherds, Luttrell and his team decide not to kill them. But one of the Afghans alerts a group of Taliban fighters to the invaders, and a terrible battle ensues, in which the SEALs find themselves hopelessly outnumbered and outgunned.",
                            "http://t1.gstatic.com/images?q=tbn:ANd9GcScjXYp5MbyDO78-AWMYL2_DYlwHoYQzrt3-DIfkxN0OQQpW0mI"
                            "https://www.youtube.com/watch?v=yoLFk4JK_RM")
the_accountant = media.Movie("The Accountant",
                             "Christian Wolff (Ben Affleck) is a mathematics savant with more affinity for numbers than people. Using a small-town CPA office as a cover, he makes his living as a freelance accountant for dangerous criminal organizations. With a Treasury agent (J.K. Simmons) hot on his heels, Christian takes on a state-of-the-art robotics company as a legitimate client. As Wolff gets closer to the truth about a discrepancy that involves millions of dollars, the body count starts to rise.",
                             "data:image/jpeg;base64,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",
                             "https://www.youtube.com/watch?v=DBfsgcswlYQ")
the_revenant = media.Movie("The Revenant",
                           "While exploring the uncharted wilderness in 1823, frontiersman Hugh Glass (Leonardo DiCaprio) sustains life-threatening injuries from a brutal bear attack. When a member (Tom Hardy) of his hunting team kills his young son (Forrest Goodluck) and leaves him for dead, Glass must utilize his survival skills to find a way back to civilization. Grief-stricken and fueled by vengeance, the legendary fur trapper treks through the snowy terrain to track down the man who betrayed him.",
                           "data:image/jpeg;base64,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",
                           "https://www.youtube.com/watch?v=LoebZZ8K5N0")
thirteen_hours = media.Movie("13 Hours",
                       "On Sept. 11, 2012, Islamic militants attack the U.S. Consulate in Benghazi, Libya, killing Ambassador J. Christopher Stevens and Sean Smith, an officer for the Foreign Service. Stationed less than one mile away are members (James Badge Dale, John Krasinski, Max Martini) of the Annex Security Team, former soldiers assigned to protect operatives and diplomats in the city. As the assault rages on, the six men engage the combatants in a fierce firefight to save the lives of the remaining Americans.",
                       "https://images-na.ssl-images-amazon.com/images/I/91zhWpXHVzL._SL1500_.jpg",
                       "https://www.youtube.com/watch?v=4CJBuUwd0Os")
john_wick = media.Movie("John Wick",
                        "Legendary assassin John Wick (Keanu Reeves) retired from his violent career after marrying the love of his life. Her sudden death leaves John in deep mourning. When sadistic mobster Iosef Tarasov (Alfie Allen) and his thugs steal John's prized car and kill the puppy that was a last gift from his wife, John unleashes the remorseless killing machine within and seeks vengeance. Meanwhile, Iosef's father (Michael Nyqvist) -- John's former colleague -- puts a huge bounty on John's head."
                        "http://is2.mzstatic.com/image/thumb/Video2/v4/3b/ea/a4/3beaa4a6-611c-cbc2-6718-fd2578abf363/source/1200x630bb.jpg",
                        "https://www.youtube.com/watch?v=2AUmvWm5ZDQ")
