
import java.util.SortedMap;
import java.util.TreeMap;

/**
 * @author Alexis Biver
 *
 * Dictionary : Object to represent the posting list of a dictionary
 *
 * Global Variables :
 * dict : HashMap<Integer,PostingList>  representing a dictionnary by a posting list and ascessing it from an Integer key
 * keyword : String                     representing the word
 */
public class Dictionary {
    private SortedMap<Integer,PostingList> dict;
    private String keyword;

    /**
     * Constructor
     */
    public Dictionary() {
        this.dict = new TreeMap<>();
    }

    /**
     * Add a term to the keywords
     * @param term String to add
     */
    public void addTerm(String term){
        this.keyword += term.length()+term;
    }

    /**
     * add a PostingList to the dictionary
     * @param p PostingList to add
     */
    public void addPostings(PostingList p){
        int i = this.dict.size();
        this.dict.put(i, p);
    }

    //TODO : a toString method
    @Override
    public String toString() {
        for (int i = 0; i < this.dict.size();i++){
            String dictString = "TODO";
        }
        return this.keyword + " : " ;
    }

    /**Setters et Getters*/

    public SortedMap<Integer, PostingList> getDict() {
        return dict;
    }

    public void setDict(SortedMap<Integer, PostingList> dict) {
        this.dict = dict;
    }

    public String getKeyword() {
        return keyword;
    }

    public void setKeyword(String keyword) {
        this.keyword = keyword;
    }

    /**------------------*/
}
