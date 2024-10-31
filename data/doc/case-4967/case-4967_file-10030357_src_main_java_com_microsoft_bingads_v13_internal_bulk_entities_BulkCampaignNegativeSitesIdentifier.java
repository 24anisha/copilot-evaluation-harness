package com.microsoft.bingads.v13.internal.bulk.entities;

import com.microsoft.bingads.v13.bulk.entities.BulkCampaignNegativeSites;
import com.microsoft.bingads.v13.internal.bulk.StringTable;
import static com.microsoft.bingads.internal.utilities.Comparer.compareNullable;

/**
 * Reserved for internal use.
 */
public class BulkCampaignNegativeSitesIdentifier extends BulkNegativeSiteIdentifier {

    /**
     * Reserved for internal use.
     */
    public long getCampaignId() {
        return this.getEntityId();
    }

    public void setCampaignId(long value) {
        this.setEntityId(value);
    }

    /**
     * Reserved for internal use.
     */
    public String getCampaignName() {
        return this.getEntityName();
    }

    public void setCampaignName(String value) {
        this.setEntityName(value);
    }

    @Override
    public MultiRecordBulkEntity createEntityWithThisIdentifier() {
        return new BulkCampaignNegativeSites(this);
    }

    @Override
    protected String getParentColumnName() {
        return StringTable.Campaign;
    }

    @Override
    public boolean equals(Object other) {
        if (!(other instanceof BulkCampaignNegativeSitesIdentifier)) {
            return false;
        }
        
        BulkCampaignNegativeSitesIdentifier otherIdentifier = (BulkCampaignNegativeSitesIdentifier) other;

        boolean isNameNotEmpty = getCampaignName() != null &&
                getCampaignName().length() != 0;

        return compareNullable(getCampaignId(), otherIdentifier.getCampaignId()) ||
                (
                        isNameNotEmpty &&
                                compareNullable(getCampaignName(), otherIdentifier.getCampaignName())
                );
    }
}
